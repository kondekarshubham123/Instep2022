from models import Drugs, User
from main import app

def insert_dummy_data():
    with app.app_context():

        # Drugs Dummy Data
        Drugs.create('ALVAC-HIV/AIDSVAX B/E','HIV vaccine','Vaccines for COVID-19 may have been developed in record time, but that achievement still eludes researchers looking to immunize people against HIV-1, and another candidate looks to have fallen by the wayside in 2020.')
        Drugs.create('Balovaptan','Autism','It’s always a big disappointment when a drug aiming to treat a condition with no approved therapies goes to the wall, and that happened this year when Roche abandoned balovaptan, which had been leading a very small field of potential therapies for autism spectrum disorder (ASD).')
        Drugs.create('Edasalonexent','Duchenne muscular dystrophy','There was more than one late-stage disappointment among companies developing drugs for the muscle-wasting disease Duchenne muscular dystrophy in 2020, but the demise of Catabasis’ edasalonexent was particularly keenly felt.')
        Drugs.create('Epanova','Mixed dyslipidemia','With its fish oil-derived drug Epanova, AstraZeneca was looking to follow in the footsteps of Amarin’s blockbuster hopeful Vascepa and show that it could cut heart risks among patients with high blood lipid levels—a category it used to dominate with its Crestor statin before it lost patent protection.')
        Drugs.create('Hydroxychloroquine','COVID-19','It stands out because it was promoted so vehemently by then-U.S. President Donald Trump, who described the drug as a “game changer” and said he had been taking it prophylactically to ward off infection—as did other public figures, such as Brazilian President Jair Bolsonaro. That trumpeting came, unfortunately, ahead of clinical results showing it had no impact on the disease.')
        Drugs.create('IW-3718','Gastroesophageal reflux disease (GERD)','At one time, Ironwood claimed its lead candidate, IW-3718, had the potential to become a $2 billion-a-year product, but that promise evaporated in September when it failed a phase 3 trial in refractory gastroesophageal reflux disease (GERD) and was canned.')
        Drugs.create('SARS-CoV-2 vaccine','COVID-19','Sometimes, even a delay to a program can have a dramatic impact on patient health. A late entrant to this list is a small trial of Sanofi and GlaxoSmithKline’s adjuvanted recombinant protein-based COVID-19 vaccine that could delay approval until the end of this year.')
        Drugs.create('Semorinemab','Alzheimer’s disease','With anti-amyloid drugs repeatedly failing to make any headway in Alzheimer’s disease, targeting tau protein has emerged as a new focus for dementia drug developers. However, a setback in September with one of the leading candidates in the anti-tau field—Roche and AC Immune’s semorinemab—suggests this target may be equally challenging.')
        Drugs.create('Tecentriq','Triple-negative breast cancer','There was jubilation among patients with triple negative breast cancer (TNBC) when Roche’s checkpoint inhibitor Tecentriq (atezolizumab) was approved to treat the disease in March 2019, becoming the first immuno-oncology option for the highly aggressive tumor—and breast cancer in general.')

        # # Organization
        User.create('pfizer@healthcare.com','Pfizer@123','Pfizer','organization')

        # Hospital
        User.create('the.royal.hospital@healthcare.com','Royal@123','Royal Hospital','Hospital')
        User.create('hammersmith.hospital@healthcare.com', 'Hammer@123', 'Hammersmith Hospital', 'Hospital')

        # Patient Dummy
        User.create('shubham.kondekar@healthcare.com','Shubham@123','Shubham', 'Patient')
        User.create('clarie03.trn@healthcare.com','Clarie@123','Clarie', 'Patient')
        User.create('jamesrobert.trn@healthcare.com','James@123','James', 'Patient')
        User.create('viyan.trn@healthcare.com','Viyan@123','Viyan', 'Patient')
