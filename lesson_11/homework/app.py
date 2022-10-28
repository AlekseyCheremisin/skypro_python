from flask import Flask, render_template

import utils

app = Flask(__name__)

data = utils.load_candidates_from_json("data/candidates.json")


@app.route('/')
def main_page():
    return render_template("list.html", candidates=data)

@app.route('/candidate/<int:uid>')
def candidate_profile(uid):
    candidate = utils.get_candidate(uid)
    return render_template("card.html", candidate=candidate)

@app.route('/search/<candidate_name>')
def search_by_name(candidate_name):
    candidates_by_name = utils.get_candidates_by_name(candidate_name)
    count = len(candidates_by_name)
    return render_template("search.html", count=count, candidates=candidates_by_name)

@app.route('/skill/<skill_name>')
def search_by_skill(skill_name):
    candidates_by_skill = utils.get_candidates_by_skill(skill_name)
    count = len(candidates_by_skill)
    return render_template("skill.html", skill=skill_name, count=count, candidates=candidates_by_skill)

app.run()