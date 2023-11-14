from lib.reading_time import *
"""
As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.
"""

#take in a parameter with text
#figure out the length of the text in words
#compare amount of words to timeframe

#Test examples:

#text under 200 words 
#text over 200 words
#200 word long string

def test_estimate_time_under_200():
    result = estimate_time("Coal is a valuable hard, black material extracted from mines. Wood that has been buried for a long time becomes coal due to a chemical change. Earthquakes cause vast forest areas to sink underground and contribute to such changes as a result of tremendous heat and pressure. Coal mines can be found in our country at  Dhanbad, Jharia, Giridih, Chaibasa, and other locations. Coal is exported from India to Japan, Nepal, and Bangladesh. Coal is used as a fuel in both homes and factories and industries. The majority of trains and steamers move by burning coal in steam engines.")
    assert result == "It would take you 0.5 minutes to read this text"

def test_estimate_time_over_200():
    result = estimate_time("Coal is a valuable hard, black material extracted from mines. Wood that has been buried for a long time becomes coal due to a chemical change. Earthquakes cause vast forest areas to sink underground and contribute to such changes as a result of tremendous heat and pressure. Coal mines can be found in our country at  Dhanbad, Jharia, Giridih, Chaibasa, and other locations. Coal is exported from India to Japan, Nepal, and Bangladesh. Coal is used as a fuel in both homes and factories and industries. The majority of trains and steamers move by burning coal in steam engines. Coal is a valuable hard, black material extracted from mines. Wood that has been buried for a long time becomes coal due to a chemical change. Earthquakes cause vast forest areas to sink underground and contribute to such changes as a result of tremendous heat and pressure. Coal mines can be found in our country at  Dhanbad, Jharia, Giridih, Chaibasa, and other locations. Coal is exported from India to Japan, Nepal, and Bangladesh. Coal is used as a fuel in both homes and factories and industries. The majority of trains and steamers move by burning coal in steam engines. Coal is a valuable hard, black material extracted from mines. Wood that has been buried for a long time becomes coal due to a chemical change. Earthquakes cause vast forest areas to sink underground and contribute to such changes as a result of tremendous heat and pressure. Coal mines can be found in our country at  Dhanbad, Jharia, Giridih, Chaibasa, and other locations. Coal is exported from India to Japan, Nepal, and Bangladesh. Coal is used as a fuel in both homes and factories and industries. The majority of trains and steamers move by burning coal in steam engines.")
    assert result == "It would take you 1.5 minutes to read this text"

def test_estimate_time_200():
    result = estimate_time("Coal is a valuable hard, black material extracted from mines. Wood that has been buried for a long time becomes coal due to a chemical change. Earthquakes cause vast forest areas to sink underground and contribute to such changes as a result of tremendous heat and pressure. Coal mines can be found in our country at  Dhanbad, Jharia, Giridih, Chaibasa, and other locations. Coal is exported from India to Japan, Nepal, and Bangladesh. Coal is used as a fuel in both homes and factories and industries. The majority of trains and steamers move by burning coal in steam engines. Coal is a valuable hard, black material extracted from mines. Wood that has been buried for a long time becomes coal due to a chemical change. Earthquakes cause vast forest areas to sink underground and contribute to such changes as a result of tremendous heat and pressure. Coal mines can be found in our country at  Dhanbad, Jharia, Giridih, Chaibasa, and other locations. Coal is exported from India to Japan, Nepal, and Bangladesh. Coal is used as a fuel in both homes and factories and industries. The majority of trains and steamers move by burning coal in steam engines.")
    assert result == "It would take you 1.0 minutes to read this text"