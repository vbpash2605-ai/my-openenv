def grade_task(task, response):
    response = response.lower()
    expected = task["expected"]

    score = 0

    for item in expected:
        if item in response:
            score += 1

    return score / len(expected)
