from PyInquirer import Separator
import ui.menu_validator as menu_validator

__menu = [
    {
        'type': 'list',
        'name': 'menu',
        'message': 'What do you want to do?',
        'choices': [
            Separator(),
            'Update Data',
            'Update Sentiment Value',
            'Show Data',
            'Visualization',
            'Quit'
        ]
    }
]

__updateData = [
    {
        'type': 'input',
        'name': 'range',
        'message': 'Pick range to Scrape (1-7 days from now) : ',
        'validate': menu_validator.RangeScrapeValidator
    },
    {
        'type': 'input',
        'name': 'max_tweet',
        'message': 'How much \'vaksin covid\' tweets u want to scrape :',
        'validate': menu_validator.RangeTweetsValidator
    },

]


def pickStartDate(startDate):
    return [
        {
            'type': 'list',
            'name': 'start_dt',
            'message': 'Pick start date :',
            'choices': startDate
        }
    ]


def pickEndDate(endDate):
    return [
        {
            'type': 'list',
            'name': 'end_dt',
            'message': 'Pick end date :',
            'choices': endDate
        }
    ]
