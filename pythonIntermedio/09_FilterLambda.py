#<<---Filter() con Lambda--->>#
numbers = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = list(filter(lambda n: n % 2 == 0, numbers))
oddNumbers = list(filter(lambda n: n % 2 == 1, numbers))

#-> Ejemplo 2
matches = [
    {
        "Home_team": "Bolivia",
        "Away_team": "Uruguay",
        "Home_team_score": 1,
        "Away_team_score": 3,
        "Home_team_result": "Lose"
    },
    {
        "Home_team": "Brazil",
        "Away_team": "Mexico",
        "Home_team_score": 1,
        "Away_team_score": 1,
        "Home_team_result": "Draw"
    },
    {
        "Home_team": "Ecuador",
        "Away_team": "Venezuela",
        "Home_team_score": 5,
        "Away_team_score": 0,
        "Home_team_result": "Win"
    }
]

matchResults = list(filter(lambda item: item["Home_team_result"], matches))