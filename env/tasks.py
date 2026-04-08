def get_tasks():
    return [
        {
            "name": "email_triage",
            "input": "Email: 'Client meeting tomorrow'",
            "expected": ["important"]
        },
        {
            "name": "code_review",
            "input": "Code: if(x=10)",
            "expected": ["bug", "=="]
        },
        {
            "name": "data_cleaning",
            "input": "Data: [1, None, 2]",
            "expected": ["remove", "1,2"]
        }
    ]
