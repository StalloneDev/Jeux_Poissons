from django.shortcuts import render, redirect
import random

# Structure des questions
questions = [
    {
        'id': 1,
        'question': "Quel poisson anime les récifs dès 3 m de profondeur ?",
        'options': ['ChirugienBlue.png', 'coffreMouton.png', 'papillon.png', 'pastenague.png'],
        'correct': 'ChirugienBlue.png',
        'info': {
            'nom': "Chirurgien Bleu",
            'habitat': "Récifs coralliens dès 3 mètres de profondeur.",
            'description': "Poisson au corps ovale de couleur bleue vive avec une queue jaune. Ce poisson joue un rôle important dans la gestion des algues sur les récifs coralliens.",
            'habitudes': "Grégaire, il vit souvent en petits groupes. Il se nourrit d'algues, jouant un rôle essentiel dans le maintien de la santé des récifs coralliens."
        }
    },
    {
        'id': 2,
        'question': "Quel poisson possède un aiguillon venimeux et vit sur les fonds sableux ?",
        'options': ['pastenague.png', 'tharzandMarquerau.png', 'coffreMouton.png', 'feeLorette.png'],
        'correct': 'pastenague.png',
        'info': {
            'nom': "Pastenague Américaine",
            'habitat': "Fonds sableux des récifs et des lagons.",
            'description': "Raie de grande taille avec une queue munie d'un aiguillon venimeux. Cette raie utilise son aiguillon pour se défendre, mais elle est généralement inoffensive si elle n’est pas dérangée.",
            'habitudes': "Se nourrit principalement de mollusques et de petits poissons enfouis dans le sable."
        }
    },
    {
        'id': 3,
        'question': "Quel poisson se nourrit de polypes de corail et vit en couple ?",
        'options': ['papillon.png', 'ChirugienBlue.png', 'coffreMouton.png', 'feeLorette.png'],
        'correct': 'papillon.png',
        'info': {
            'nom': "Papillon Pyjama",
            'habitat': "Récifs coralliens peu profonds.",
            'description': "Petit poisson aux couleurs vives avec des rayures verticales distinctes.",
            'habitudes': "Il vit en couple et se nourrit exclusivement de polypes de corail, contribuant à l'équilibre de l'écosystème récifal."
        }
    },
    {
        'id': 4,
        'question': "Quel poisson vit dans les récifs proéminents et défend les algues qu’il mange ?",
        'options': ['sergentMajor.png', 'tharzandMarquerau.png', 'BaracudaJaune.png', 'coffreMouton.png'],
        'correct': 'sergentMajor.png',
        'info': {
            'nom': "Sergent Major",
            'habitat': "Principalement dans les récifs coralliens proéminents",
            'description': "Petit poisson rayé de noir et jaune, souvent vu en bancs. Ce petit poisson est territorial et protège ses algues, un rôle important pour la santé des récifs.",
            'habitudes': "Très territorial, il protège son espace dans les récifs. Il se nourrit de petites algues et de plancton."
        }
    },
    {
        'id': 5,
        'question': "Quel carnassier pélagique peut atteindre 1,20 m et vit dans les eaux profondes ?",
        'options': ['pastenague.png', 'tharzandMarquerau.png', 'BaracudaJaune.png', 'coffreMouton.png'],
        'correct': 'tharzandMarquerau.png',
        'info': {
            'nom': "Thazard Maquereau",
            'habitat': "Zone pélagique (eaux profondes), mais aussi près des côtes.",
            'description': " Grand poisson pouvant atteindre 1,20 mètre, avec un corps fuselé argenté.",
            'habitudes': "Prédateur carnassier, il chasse des bancs de petits poissons. C'est un nageur rapide, souvent solitaire."
        }
    },
    {
        'id': 6,
        'question': "Quel poisson à la mâchoire puissante, et est présent dans les herbiers marins  ?",
        'options': ['papillon.png', 'ChirugienBlue.png', 'BaracudaJaune.png', 'coffreMouton.png'],
        'correct': 'BaracudaJaune.png',
        'info': {
            'nom': "Barracuda Jeune",
            'habitat': "Présent dans les herbiers marins et près des récifs.",
            'description': "Prédateur à la mâchoire puissante, avec un corps long et élancé, souvent argenté.",
            'habitudes': "Les jeunes barracudas se cachent dans les herbiers marins pour éviter les prédateurs et chasser de petits poissons. Ils deviennent plus solitaires en grandissant."
        }
    },
    {
        'id': 7,
        'question': "Quel poisson est souvent caché dans les anfractuosités des récifs coralliens et ne sort qu’à la nuit tombée ?",
        'options': ['papillon.png', 'tharzandMarquerau.png', 'cardinalEpine.png', 'coffreMouton.png'],
        'correct': 'cardinalEpine.png',
        'info': {
            'nom': "Cardinal longue épine",
            'habitat': " Anfractuosités des récifs coralliens, surtout à plus grande profondeur durant la journée.",
            'description': "Petit poisson rouge à longue épine dorsale.",
            'habitudes': "Nocturne, il sort la nuit pour se nourrir, principalement de petits invertébrés et de plancton."
        }
    },
    {
        'id': 8,
        'question': "Quel poisson est souvent caché dans les anfractuosités des récifs coralliens et ne sort qu’à la nuit tombée ?",
        'options': ['papillon.png', 'tharzandMarquerau.png', 'cardinalEpine.png', 'coffreMouton.png'],
        'correct': 'cardinalEpine.png',
        'info': {
            'nom': "Cardinal longue épine",
            'habitat': " Anfractuosités des récifs coralliens, surtout à plus grande profondeur durant la journée.",
            'description': "Petit poisson rouge à longue épine dorsale.",
            'habitudes': "Nocturne, il sort la nuit pour se nourrir, principalement de petits invertébrés et de plancton."
        }
    },
]

def index(request):
    request.session['score'] = 0
    return render(request, 'quiz/index.html')

def question(request, question_id):
    # Vérifier si la question existe
    if question_id > len(questions):
        return redirect('end_quiz', score=request.session.get('score', 0))

    question_data = questions[question_id - 1]
    random.shuffle(question_data['options'])
    selected_option = request.POST.get('selected_option')
    correct = selected_option == question_data['correct']

    # Mettre à jour le score si la réponse est correcte
    if correct:
        request.session['score'] += 1

    next_question = question_id + 1 if question_id < len(questions) else None

    # Rediriger vers la question suivante ou vers la fin
    if next_question is None:
        return redirect('end_quiz', score=request.session['score'], question_id=question_id)

    return render(request, 'quiz/question.html', {
        'question': question_data,
        'total_questions': len(questions),
        'score': request.session['score'],
        'next_question': next_question
    })


def result(request, question_id):
    selected_option = request.POST.get('selected_option')
    question_data = questions[question_id - 1]
    correct = selected_option == question_data['correct']
    
    # Initialiser ou récupérer le nombre de tentatives restantes
    attempt_left = request.session.get('attempts', 2)

    if correct:
        request.session['score'] = request.session.get('score', 0) + 1
        attempt_left = 2  # Réinitialiser les tentatives pour la prochaine question
    else:
        attempt_left -= 1

    # Mettre à jour le nombre de tentatives dans la session
    request.session['attempts'] = attempt_left

    # Déterminer la question suivante ou la fin du quiz
    next_question = question_id + 1 if question_id < len(questions) else None

    # Si le joueur échoue deux fois (tentatives restantes = 0), afficher le message d'échec et les infos
    if attempt_left == 0:
        request.session['attempts'] = 2  # Réinitialiser pour la prochaine question
        return render(request, 'quiz/result.html', {
            'question': question_data,
            'correct': False,
            'selected_option': selected_option,
            'info': question_data['info'],  # Afficher les infos sur la bonne réponse
            'next_question': next_question,
            'score': request.session['score'],
            'total_questions': len(questions),
            'attempt_left': attempt_left,
        })

    # Si c'était la dernière question, rediriger vers la fin du quiz
    if next_question is None:
        score = request.session['score']
        return redirect('end_quiz', score=score, question_id=question_id)

    # Afficher la page de résultat standard si la tentative est valide
    return render(request, 'quiz/result.html', {
        'question': question_data,
        'correct': correct,
        'selected_option': selected_option,
        'info': question_data['info'] if correct else None,
        'next_question': next_question,
        'score': request.session['score'],
        'total_questions': len(questions),
        'attempt_left': attempt_left,
    })

def end_quiz(request, score, question_id):
    # Calcul du total des points (une bonne réponse = 5 points)
    question_data = questions[question_id - 1]
    score_final = score * 5

    # Détermination du trophée à afficher
    if score >= 7:
        trophée = 'or'
    elif 5 <= score <= 6:
        trophée = 'argent'
    elif 3 <= score <= 4:
        trophée = 'bronze'
    else:
        trophée = 'emogie'

    return render(request, 'quiz/end.html', {
        'score': score,
        'score_final': score_final,
        'trophée': trophée,
        'question': question_data,
        'total_questions': len(questions),
    })




# def question(request, question_id):
#     if question_id > len(questions):
#         return redirect('end_quiz', score=request.session.get('score', 0))

#     question_data = questions[question_id - 1]
#     selected_option = request.POST.get('selected_option')
    
    
#     if 'attempts' not in request.session:
#         request.session['attempts'] = 0

#     if selected_option:
#         correct = selected_option == question_data['correct']

#         if correct:
#             request.session['score'] += 1
#             request.session['attempts'] = 0  
#         else:
#             request.session['attempts'] += 1
#             if request.session['attempts'] >= 2:
#                 return redirect('end_quiz', score=request.session['score'])

#     next_question = question_id + 1 if question_id < len(questions) else None

#     if next_question is None:
#         return redirect('end_quiz', score=request.session['score'], question_id=question_id)

#     return render(request, 'quiz/question.html', {
#         'question': question_data,
#         'total_questions': len(questions),
#         'score': request.session['score'],
#         'next_question': next_question
#     })