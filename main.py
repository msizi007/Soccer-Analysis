from models.predict import predict_xG, get_score_probabilities, calc_odds
from models import LEAGUE, ALL_CLUBS

def predict(home, away):
    print(home.name, away.name)
    
    hx, ax = predict_xG(LEAGUE, home, away)
    print(f'XG: ', hx, ax)

    fs, w, d, l = get_score_probabilities(hx, ax)
    print(f'''
final score: {fs}
win %: {w}
draw %: {d}
lose %: {l}
          ''')
    
    ho, do, ao = calc_odds(w, d, l)
    print('Odds: ', ho, do, ao)
    
predict(ALL_CLUBS[0], ALL_CLUBS[8])
