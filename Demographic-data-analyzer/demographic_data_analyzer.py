import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    # Path : D:\Computer Science\Data Analysis with Python-FCC.org\Boilerplate-demographic-data-analyzer\adult.data.csv
    df = pd.read_csv(
        r'D:\\Computer Science\\Data Analysis with Python-FCC.org\\Boilerplate-demographic-data-analyzer\\adult.data.csv')
    n = df.shape[0]  # Number of entries
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = (df[df['sex'] == 'Male'].age.mean()).round(1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = (
        (df['education'].value_counts()['Bachelors']/n)*100).round(1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df['education'].isin(
        ['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(
        ['Bachelors', 'Masters', 'Doctorate'])]

    # percentage with salary >50K
    a = higher_education[higher_education['salary'] == '>50K'].count()
    b = higher_education.count()
    higher_education_rich = (a/b)*100
    higher_education_rich = higher_education_rich.round(1)[0]

    a = lower_education[lower_education['salary'] == '>50K'].count()
    b = lower_education.count()
    lower_education_rich = (a/b)*100
    lower_education_rich = lower_education_rich.round(1)[0]

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    num_min_workers_rich = num_min_workers[num_min_workers['salary'] == '>50K']
    a = num_min_workers_rich.shape[0]
    b = num_min_workers.shape[0]

    rich_percentage = (a*100)//b

    # What country has the highest percentage of people that earn >50K?
    rich_df = df[df['salary'] == '>50K']
    rich_df = rich_df.groupby(by='native-country').count()
    rich_df = rich_df['age']
    sample_df = df.groupby(by='native-country').count()
    sample_df = sample_df['age']
    country, perc = '', -1.0
    for c, n in rich_df.items():
        p = (n*100)/sample_df[c]
        if perc < p:
            perc = p
            country = c

    highest_earning_country = country
    highest_earning_country_percentage = round(perc, 1)

    # Identify the most popular occupation for those who earn >50K in India.
    in_df = df[df['native-country'] == 'India']
    in_df_rich = in_df[in_df['salary'] == '>50K']
    in_df_rich = in_df_rich.groupby(by='occupation').count()
    in_df_rich = in_df_rich['age']
    count, job = 0, ''
    for item in in_df_rich.items():
        if item[1] > count:
            count = item[1]
            job = item[0]
    top_IN_occupation = job

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(
            f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(
            f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(
            f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(
            f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
