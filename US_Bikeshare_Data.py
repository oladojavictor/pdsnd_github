import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
month_list = ['all', 'january', 'february', 'march', 'april' , 'may', 'june']
day_list = ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    
    city = input('Please, enter the city you would like analyze among chicago, new york city and washington: ').lower()
    while city not in CITY_DATA.keys():
        print('\ninvalid input, please re-enter the city\n')
        city = input('\nPlease, enter the city you would like to analyze among chicago, new york city and washington: \n').lower()
        
    month = input("Please, enter the name of the month you would like filter with.\n you should enter 'all' if no filter: " ).lower()
    while month not in month_list:
        print('\n invalid input, please re-enter the month')
        month = input("Please, enter the name of the month you would like filter with.\n you should enter 'all' if no filter: ").lower()
        
    day = input("\nPlease, enter the name of the day you would like filter with.\n you should enter 'all' if no filter: " ).lower()
    while day not in day_list:
        print('\n invalid input, please re-enter the day')
        day = input("\nPlease, enter the name of the day you would like filter with.\n you should enter 'all' if no filter: " ).lower()
        
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        month = month_list.index(month)
        df = df[df['month']== month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month = df['month'].mode()[0]
    print('\nMost Common Month:', month)

    # TO DO: display the most common day of week
    day_week = df['day_of_week'].mode()[0]
    print('\nMost Common Day of Week:', day_week)

    # TO DO: display the most common start hour
    start_hour = df['hour'].mode()[0]
    print('\nMost Common Start Hour:',start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('\nMost common used start station:', start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('\nMost common used end station:', end_station)

    # TO DO: display most frequent combination of start station and end station trip
    start_end_station = (df['Start Station'] + ' ' + 'and'+ ' '+ df['End Station']).mode()[0]
    print('\nMost frequent combination of start and end station trip:',start_end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip = df['Trip Duration'].sum()
    print('\nTotal Travel Time:', total_trip)

    # TO DO: display mean travel time
    mean_trip = df['Trip Duration'].mean()
    print('\nMean Travel Time:', mean_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_type = df['User Type'].value_counts()
    print('\ncounts of users types:\n', count_user_type)
    
    # TO DO: Display counts of gender

    if city == 'washington':
            print('\nNo gender and birth year data for washington')
    else:
       
        count_gender = df['Gender'].value_counts()
        print('\ncounts of gender:\n', count_gender)
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()[0]
        print('\nearliest, most recent, and most common years of birth are \n{},\n{},\n{}\nrespectively'.format(earliest_birth_year,most_recent_birth_year,most_common_birth_year))

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """Displays statistics on bikeshare users."""

    print('\nAsking information about raw data...\n')
    start_time = time.time()
    #TO DO: Display raw trip data five at a time 
    start_location = 0
    question = input('\nWould you like to see 5 rows of individual trip data? Enter yes or no\n').lower()
    while question == 'yes':
        #print first five raw data
        print(df.iloc[start_location:start_location+5])
        start_location += 5
        question = input('\nWould you like to see the next 5 rows of individual trip data? Enter yes or no\n').lower()
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()