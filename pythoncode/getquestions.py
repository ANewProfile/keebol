from qbreader import Sync as qbr

sync_client = qbr()

def get_tossup():
    tossup = sync_client.random_tossup()
    
    print(tossup.question_sanitized)
    print(tossup.answer_sanitized)