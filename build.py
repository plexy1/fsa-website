#!/usr/bin/env python3
"""Builds the FSA site. Edit the content below, then run:  python3 build.py"""
from html import escape as e
from pathlib import Path

ROOT = Path(__file__).parent
LINKTREE = "https://linktr.ee/FSAYU"
LINKEDIN = "https://www.linkedin.com/company/finance-student-association/"
INSTAGRAM = "https://www.instagram.com/fsayorku/"
EMAIL = "fsayorku@gmail.com"
YEAR = "2025 – 2026"

# ───────────────────────── content ─────────────────────────
# (name, role, photo file in assets/team or None, LinkedIn URL or None)
TEAM = [
    ("Co-Presidents", "co-presidents", [
        ("Essa Ahmed Ansari", "President", "essa-ahmed-ansari", "https://www.linkedin.com/in/essa-ansari/"),
        ("Davidson Ajay", "Co-President", "davidson-ajay", "https://www.linkedin.com/in/davidsonajay/"),
    ]),
    ("Student Alumni Advisors", "alumni-advisors", [
        ("Kevin-Khanim Mooshy", "Alumni Advisor", "kevin-khanim-mooshy", "https://www.linkedin.com/in/kevin-khanim-mooshy/"),
        ("Cyrus Naumoski", "Alumni Advisor", "cyrus-naumoski", "https://www.linkedin.com/in/cyrus-naumoski-238062225/"),
        ("Fadil Siddiqui", "Alumni Advisor", "fadil-siddiqui", "https://www.linkedin.com/in/fadilsiddiqui/"),
        ("Lara Abughazal", "Alumni Advisor", "lara-abughazal", "https://www.linkedin.com/in/lara-abughazal/"),
    ]),
    ("Marketing", "marketing", [
        ("Jaiden Katsoras", "VP Marketing", "jaiden-katsoras", "https://www.linkedin.com/in/jaiden-katsoras-96829a268/"),
        ("Trinh Vo", "Director", None, None),
        ("Kim Taï Franco", "Director", "kim-tai-franco", "https://www.linkedin.com/in/kim-ta%C3%AF-franco-0949632a1"),
    ]),
    ("Finance", "finance", [
        ("Adam Jaffar", "VP Finance", "adam-jaffar", "https://www.linkedin.com/in/adamjaffar"),
        ("Bhuvanjot Arneja", "Director", "bhuvanjot-arneja", None),
        ("Reet Sharma", "Director", "reet-sharma", "https://www.linkedin.com/in/reetsharmaybe/"),
        ("Vladislav Moisei", "Director", "vladislav-moisei", "https://www.linkedin.com/in/vladislav-moisei-582696271/"),
    ]),
    ("External Affairs", "external-affairs", [
        ("Melissa Lam", "VP External Affairs", "melissa-lam", "https://www.linkedin.com/in/melissa-lam-kwoh-hing"),
        ("Jahra Islam", "Director", "jahra-islam", "https://www.linkedin.com/in/jahra-islam/"),
        ("Shervin Maadani", "Director", "shervin-maadani", "https://www.linkedin.com/in/shervin-maadani-47716028b/"),
        ("Brandon", "Director", "brandon", None),
        ("Ahmed", "Director", None, None),
    ]),
    ("Internal Affairs", "internal-affairs", [
        ("Deborah George-Nsoribe", "VP Internal Affairs", "deborah-george-nsoribe", "https://www.linkedin.com/in/deborah-george-nsoribe/"),
        ("Nuzaira Aruba Azad", "Director", "nuzaira-aruba-azad", "https://www.linkedin.com/in/nuzairaa2004/"),
        ("Vladsylav Kalnauz", "Director", "vladsylav-kalnauz", "https://www.linkedin.com/in/vladkalnauz/"),
    ]),
    ("Operations & Projects", "operations-projects", [
        ("Hangthirith Tek", "VP Operations & Projects", "hangthirith-tek", "https://www.linkedin.com/in/hangthirith-tek/"),
        ("Michael Di Luca", "Director", "michael-di-luca", "https://www.linkedin.com/in/michaeldiluca24"),
        ("Tabish Mohamad Hashram", "Director", "tabish-mohamad-hashram", "https://www.linkedin.com/in/tabishhasham"),
    ]),
]

ADVISORS = [
    ("Prof. Nadeem Kassam", "prof-nadeem-kassam", "https://www.yorku.ca/laps/connections-mentor/nadeem-kassam/",
     "Prof. Nadeem is a seasoned investment professional with over 15 years of experience in portfolio management, trading, equity research, and investment strategy, gained through roles at leading Canadian and global banks. He is the Chief Investment Strategist and Chief Operating Officer at Marnoa Private Wealth Counsel Ltd. Prior to this, Nadeem founded Advisor Insights, a consulting practice supporting financial advisors managing over $2 billion in client assets."),
    ("Prof. Saikat Sarkar", "prof-saikat-sarkar", "https://profiles.laps.yorku.ca/profiles/sarkars/",
     "Prof. Saikat is an assistant professor in the School of Administrative Studies at York University. He has been a visiting scholar at the Melbourne University, Australia. Dr. Sarkar previously taught several undergraduate and graduate finance courses in Tampere University, Finland, Jyvaskyla University, Finland, and Mount Allison University, New Brunswick, Canada."),
    ("Prof. Nabil Tahani", "prof-nabil-tahani", "https://profiles.laps.yorku.ca/profiles/ntahani/",
     "Prof. Nabil Tahani received his PhD in Finance from HEC Montréal. He also has an Engineering degree in Applied Mathematics and Computer Science from the École Nationale des Ponts et Chaussées, Paris, a MSc in Probability and Finance from Pierre and Marie Curie University, Paris, and a MSc in Mathematical Modelling in Economics from La Sorbonne, Paris."),
    ("Prof. Daniel Richards", "prof-daniel-richards", "https://profiles.laps.yorku.ca/profiles/danwrich/",
     "Prof. Daniel is an Associate Professor in the School of Administrative Studies. He teaches personal financial planning. His research interests are behavioural finance, financial planning and investment decision making."),
]

SESSIONS = [
    ("Program Kickoff + Careers in Finance", "Kickoff"),
    ("Resume and Cover Letter Writing", "Paper"),
    ("Networking Deep Dive", "People"),
    ("Understanding the Recruitment Process", "Process"),
    ("Interview Prep (Behaviorals and Technicals)", "Interviews"),
]

LEADS = [
    ("Prabhjot Kaur", "Sales & Trading @ Scotiabank", "prabhjot-kaur", "https://www.linkedin.com/in/prabhjot-kaur-b83371200/"),
    ("Daksh Singh", "Trade Control Co-op @ CIBC Capital Markets", "daksh-singh", "https://www.linkedin.com/in/daksh-singh-111989257/"),
    ("Gopal Vasir", "Summer Analyst @ Scotiabank", "gopal-vasir", "https://www.linkedin.com/in/gopalvasir2003/"),
]

MENTORS = [
    ("Deborah George-Nsoribe", "Mentor", "mentor-deborah", "https://www.linkedin.com/in/deborah-george-nsoribe/"),
    ("Rachel Iskandar", "Mentor", "rachel-iskandar", "https://www.linkedin.com/in/rachel-iskandar-801092205/"),
    ("Essa Ansari", "Mentor", "mentor-essa-ansari", "https://www.linkedin.com/in/essa-ansari/"),
    ("Adam Jaffar", "Mentor", "mentor-adam-jaffar", "https://www.linkedin.com/in/adamjaffar/"),
    ("Kevin Catalusian", "Mentor", "kevin-catalusian", "https://www.linkedin.com/in/kevincatulusi"),
    ("Sedonia Vu", "Mentor", "sedonia-vu", None),
    ("Ahmed Hamdy", "Mentor", "ahmed-hamdy", "https://www.linkedin.com/in/ahmed-hamdy-7b439329a"),
    ("Davidson Ajay", "Mentor", "mentor-davidson-ajay", "https://www.linkedin.com/in/davidsonajay/"),
]

UPCOMING = [
    ("Feb 11", "FSA × BBSA: Breaking into Finance", LINKTREE),
    ("TBD", "Surprise Event", None),
]

PAST_EVENTS = [
    ("The Finance Forum", "event-1", "Flagship",
     "The Finance Forum, one of our most significant and engaging events of the year. The evening brought together industry professionals, faculty, and aspiring finance students for an insightful discussion on careers in finance, market trends, and the evolving landscape of the industry."),
    ("Exploring Careers in Finance", "event-2", "Workshop",
     "Workshop designed for students considering diverse career streams of finance featuring valuable key speakers from &Capital and Cross Border Impact Ventures."),
    ("Leadership in Finance", "event-3", "Networking",
     "An insightful event that allowed finance students to explore internships, strengthen career development and gain leadership skills through networking and expert guidance."),
    ("FSA × MLSE", "event-4", "Firm trek",
     "An exclusive event in networking with MLSE professionals at the Coca-Cola Coliseum, followed by a Toronto Marlies game!"),
]

MISSION = ("To bridge the gap between classroom knowledge and the financial industry by equipping students with "
           "the technical skills, professional exposure, and leadership experience needed to thrive in competitive finance careers.")

TICKER = ["Investment Banking", "Private Equity", "Asset Management", "Consulting", "Sales & Trading", "Capital Markets"]

NAV = [("Team", "team.html"), ("Advisors", "advisors.html"), ("Events", "events.html"), ("Program", "program.html")]

# ───────────────────────── pieces ─────────────────────────
ARROW = '<svg class="ar" viewBox="0 0 16 16" aria-hidden="true"><path d="M4 12 12 4M5.5 4H12v6.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="square"/></svg>'


def initials(name):
    parts = [p for p in name.replace("-", " ").split() if p[0].isalpha()]
    return (parts[0][0] + (parts[-1][0] if len(parts) > 1 else "")).upper()


def person(p, folder="team", cls=""):
    name, role, photo, url = p
    if photo:
        img = f'<img src="assets/{folder}/{photo}.jpg" alt="{e(name)}" loading="lazy" width="640" height="640">'
    else:
        img = f'<span class="mono-tile" aria-hidden="true">{initials(name)}</span>'
    inner = (f'<div class="person__img">{img}{ARROW if url else ""}</div>'
             f'<div class="person__meta"><h3>{e(name)}</h3><p>{e(role)}</p></div>')
    if url:
        return (f'<a class="person {cls} rv" href="{e(url)}" target="_blank" rel="noopener" '
                f'aria-label="{e(name)}, {e(role)} — LinkedIn">{inner}</a>')
    return f'<div class="person {cls} rv">{inner}</div>'


def head(title, desc, page):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="theme-color" content="#0d0e12">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%230d0e12'/%3E%3Cpath d='M7 22 13 15l4 4 8-10' fill='none' stroke='%23d6ff3f' stroke-width='3'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400..800&family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
<script>document.documentElement.classList.add('js')</script>
</head>
<body class="page-{page}">
<a class="skip" href="#main">Skip to content</a>
<header class="nav" id="nav">
  <a class="brand" href="index.html" aria-label="FSA — home"><span class="brand__mark">FSA<i></i></span><span class="brand__sub">Finance Students’ Association<br>York University</span></a>
  <nav class="nav__links" aria-label="Primary">
    {"".join(f'<a href="{h}"{" aria-current=page" if h.startswith(page) else ""}>{t}</a>' for t, h in NAV)}
  </nav>
  <a class="btn btn--acid nav__cta" href="join.html">Join FSA {ARROW}</a>
  <button class="nav__toggle" aria-expanded="false" aria-controls="menu"><span></span><span></span><b>Menu</b></button>
</header>
<div class="menu" id="menu" hidden>
  <nav aria-label="Mobile">
    <a href="index.html">Home</a>
    {"".join(f'<a href="{h}">{t}</a>' for t, h in NAV)}
    <a href="join.html" class="menu__join">Join FSA {ARROW}</a>
  </nav>
  <p class="menu__foot"><a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a> · <a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a></p>
</div>
<main id="main">
'''


def foot():
    return f'''</main>
<footer class="foot">
  <div class="wrap">
    <div class="foot__top">
      <p class="foot__pitch">Invest in your future with a community that helps you grow <em>faster</em> than you can on your own.</p>
      <a class="btn btn--acid btn--lg" href="join.html">Join FSA {ARROW}</a>
    </div>
    <div class="foot__cols">
      <div><h4>Explore</h4><a href="index.html">Home</a><a href="team.html">The Team</a><a href="advisors.html">Advising Committee</a><a href="events.html">Events</a><a href="program.html">Development Program</a><a href="join.html">Join FSA</a></div>
      <div><h4>Connect</h4><a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn {ARROW}</a><a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram {ARROW}</a><a href="{LINKTREE}" target="_blank" rel="noopener">Linktree {ARROW}</a><a href="mailto:{EMAIL}">{EMAIL}</a></div>
      <div><h4>Find us</h4><p>York University<br>Toronto, Ontario</p></div>
    </div>
  </div>
  <div class="foot__mark" aria-hidden="true">FSA</div>
  <div class="wrap foot__base"><span>© <span data-year>2026</span> Finance Students’ Association</span><span>York University, Toronto</span></div>
</footer>
<script src="script.js" defer></script>
</body>
</html>
'''


def page_hero(kicker, title, intro=""):
    return f'''<section class="phero">
  <div class="wrap">
    <p class="kicker rv">{kicker}</p>
    <h1 class="rv">{title}</h1>
    {f'<p class="phero__intro rv">{intro}</p>' if intro else ''}
  </div>
</section>
'''


def ticker():
    items = "".join(f"<span>{e(t)}</span><i>▲</i>" for t in TICKER)
    return f'<div class="ticker" aria-hidden="true"><div class="ticker__track">{items}{items}{items}{items}</div></div>'


# ───────────────────────── pages ─────────────────────────
def home():
    execs = [p for _, _, ppl in TEAM for p in ppl]
    faces = "".join(
        (f'<img src="assets/team/{p[2]}.jpg" alt="" loading="lazy" width="160" height="160">' if p[2]
         else f'<span class="mono-tile">{initials(p[0])}</span>') for p in execs)
    sessions = "".join(
        f'<li class="rv"><span class="syl__n">S{i}</span><span class="syl__t">{e(t)}</span><span class="syl__k">{e(k)}</span></li>'
        for i, (t, k) in enumerate(SESSIONS, 1))
    events = "".join(
        f'<a class="ecard rv" href="events.html#past"><img src="assets/events/{img}.jpg" alt="" loading="lazy" width="1280" height="960">'
        f'<span class="tag">{e(tag)}</span><h3>{e(t)}</h3></a>' for t, img, tag, _ in PAST_EVENTS)
    stats = [(len(execs), "Executives & advisors"), (len(TEAM) - 2, "Portfolios"), (len(ADVISORS), "Faculty advisors"), (len(MENTORS), "Program mentors")]
    stat_html = "".join(f'<div class="stat rv"><b data-count="{n}">{n}</b><span>{e(l)}</span></div>' for n, l in stats)
    return head("FSA — Finance Students’ Association at York University", MISSION, "index") + f'''
<section class="hero">
  <canvas class="hero__chart" id="chart" aria-hidden="true"></canvas>
  <div class="wrap hero__in">
    <p class="kicker"><span class="live"></span>Finance Students’ Association · York University, Toronto</p>
    <h1>Turn ambition<br>into <em>offers.</em></h1>
    <div class="hero__row">
      <p>We bridge the gap between classroom knowledge and the financial industry — technical skills, professional exposure and leadership experience for students breaking into finance.</p>
      <div class="hero__cta">
        <a class="btn btn--acid btn--lg" href="join.html">Join FSA {ARROW}</a>
        <a class="btn btn--line btn--lg" href="program.html">Development Program</a>
      </div>
    </div>
  </div>
  {ticker()}
</section>

<section class="sec mission">
  <div class="wrap">
    <p class="kicker rv">Our mission</p>
    <p class="mission__text rv">To <em>bridge the gap</em> between classroom knowledge and the financial industry by equipping students with the technical skills, professional exposure, and leadership experience needed to thrive in <em>competitive finance careers.</em></p>
    <div class="stats">{stat_html}</div>
  </div>
</section>

<section class="sec sec--ink program-teaser">
  <div class="wrap split">
    <div class="split__a">
      <p class="kicker rv">FSA Development Program</p>
      <h2 class="rv">Have aspirations of <em>breaking into</em> finance?</h2>
      <p class="lead rv">The FSA Development Program will give you the playbook and support you in your mission, from resume and cover-letter polishing to technical training, delivered by interns and alumni who’ve landed roles across IB, PE, AM, and Consulting.</p>
      <p class="rv">Join the cohort, learn what actually moves the needle, and turn ambition into offers.</p>
      <a class="btn btn--acid rv" href="program.html">Learn more {ARROW}</a>
    </div>
    <ol class="syl split__b">{sessions}</ol>
  </div>
</section>

<section class="sec events-teaser">
  <div class="wrap">
    <div class="sec__head">
      <div><p class="kicker rv">Events at FSA</p><h2 class="rv">One <em>high-value</em> session at a time.</h2></div>
      <div class="sec__aside rv"><p>From hands-on workshops to recruiter panels and firm treks, FSA events are designed to level up your recruiting prep and expand your network.</p><a class="btn btn--ink" href="events.html">All events {ARROW}</a></div>
    </div>
  </div>
  <div class="rail"><div class="rail__in">{events}</div></div>
</section>

<section class="sec sec--paper team-teaser">
  <div class="wrap split split--rev">
    <div class="split__a">
      <p class="kicker rv">Executive team {YEAR}</p>
      <h2 class="rv">The people <em>behind</em> FSA.</h2>
      <p class="lead rv">{len(execs)} students and alumni across marketing, finance, external affairs, internal affairs and operations — guided by an advising committee of York University faculty.</p>
      <div class="btns rv"><a class="btn btn--ink" href="team.html">Meet the team {ARROW}</a><a class="btn btn--line-ink" href="advisors.html">Advising committee</a></div>
    </div>
    <a class="faces split__b rv" href="team.html" aria-label="Meet the team">{faces}</a>
  </div>
</section>

<section class="join-band">
  <div class="wrap">
    <p class="kicker rv">Join us</p>
    <h2 class="rv">Grow faster than you can <em>on your own.</em></h2>
    <div class="join-band__row rv">
      <p>The FSA brings together driven students, mentors, and alumni to help you break into finance and thrive.</p>
      <a class="btn btn--acid btn--lg" href="join.html">Join {ARROW}</a>
    </div>
  </div>
</section>
''' + foot()


def team():
    jump = "".join(f'<a href="#{slug}">{e(t)}</a>' for t, slug, _ in TEAM)
    blocks = ""
    for i, (t, slug, ppl) in enumerate(TEAM, 1):
        cards = "".join(person(p) for p in ppl)
        blocks += f'''<section class="dept" id="{slug}">
  <div class="dept__head rv"><span class="idx">{i:02d}</span><h2>{e(t)}</h2><p>{len(ppl)} {"people" if len(ppl) != 1 else "person"}</p></div>
  <div class="people">{cards}</div>
</section>
'''
    n = sum(len(p) for _, _, p in TEAM)
    return head("The Team — FSA York University", f"Meet the FSA Executive Team {YEAR}.", "team") + page_hero(
        f"The team · {YEAR}", "Executive <em>team.</em>",
        f"{n} students and alumni running the Finance Students’ Association at York University this year.") + f'''
<div class="jump"><div class="wrap"><span>Jump to</span>{jump}</div></div>
<div class="wrap depts">
{blocks}</div>
<section class="band">
  <div class="wrap band__in rv"><h2>Guided by <em>faculty.</em></h2><p>Our advising committee is made up of distinguished professors from York University.</p><a class="btn btn--ink" href="advisors.html">Advising committee {ARROW}</a></div>
</section>
''' + foot()


def advisors():
    rows = ""
    for i, (name, photo, url, bio) in enumerate(ADVISORS, 1):
        rows += f'''<article class="prof rv">
  <span class="idx">{i:02d}</span>
  <img src="assets/advisors/{photo}.jpg" alt="{e(name)}" loading="lazy" width="640" height="640">
  <div class="prof__name"><h2>{e(name)}</h2><a class="tlink" href="{e(url)}" target="_blank" rel="noopener">York University profile {ARROW}</a></div>
  <p class="prof__bio">{e(bio)}</p>
</article>
'''
    return head("Advising Committee — FSA York University", "FSA's Advising Committee of York University professors.", "advisors") + page_hero(
        "Advising committee", "Guided by <em>faculty.</em>",
        "FSA’s Advising Committee is composed of distinguished professors from York University who provide strategic guidance, academic insight, and mentorship to help FSA align its initiatives with the evolving landscape of finance and economics. Their expertise supports the Association’s mission to bridge the gap between academic learning and professional application.") + f'''
<section class="sec">
  <div class="wrap">
    <p class="kicker rv">The committee members</p>
    <div class="profs">{rows}</div>
  </div>
</section>
''' + foot()


def events():
    up = ""
    for date, title, url in UPCOMING:
        action = (f'<a class="btn btn--acid" href="{e(url)}" target="_blank" rel="noopener">Sign up {ARROW}</a>'
                  if url else '<span class="chip">Details soon</span>')
        up += f'<li class="rv"><span class="up__date">{e(date)}</span><h3>{e(title)}</h3>{action}</li>'
    past = ""
    for i, (t, img, tag, body) in enumerate(PAST_EVENTS, 1):
        past += f'''<article class="pevent rv">
  <figure><img src="assets/events/{img}.jpg" alt="{e(t)}" loading="lazy" width="1280" height="960"></figure>
  <div><span class="idx">{i:02d}</span><span class="tag tag--ink">{e(tag)}</span><h3>{e(t)}</h3><p>{e(body)}</p></div>
</article>
'''
    return head("Events — FSA York University", "Workshops, recruiter panels and firm treks from the Finance Students' Association.", "events") + page_hero(
        "Events", "In the <em>room.</em>",
        "From hands-on workshops to recruiter panels and firm treks, FSA events are designed to level up your recruiting prep and expand your network one high-value session at a time.") + f'''
<section class="sec sec--ink upcoming">
  <div class="wrap">
    <p class="kicker rv"><span class="live"></span>FSA upcoming events</p>
    <ul class="up">{up}</ul>
  </div>
</section>
<section class="sec" id="past">
  <div class="wrap">
    <p class="kicker rv">Past events</p>
    <div class="pevents">{past}</div>
  </div>
</section>
''' + foot()


def program():
    sessions = "".join(
        f'<li class="rv"><span class="syl__n">Session {i}</span><span class="syl__t">{e(t)}</span><span class="syl__k">{e(k)}</span></li>'
        for i, (t, k) in enumerate(SESSIONS, 1))
    leads = "".join(person(p, "program", "person--lead") for p in LEADS)
    mentors = "".join(person(p, "program") for p in MENTORS)
    return head("Development Program — FSA York University", "A structured, peer-led program for navigating finance recruitment.", "program") + page_hero(
        "FSA Development Program", "The <em>playbook</em> for recruiting.",
        "Have aspirations of breaking into finance? Join the cohort, learn what actually moves the needle, and turn ambition into offers.") + f'''
<section class="sec">
  <div class="wrap split">
    <div class="split__a"><p class="kicker rv">What is the Development Program?</p>
      <p class="big rv">A structured, <em>peer-led</em> initiative designed to support students in navigating the highly competitive recruitment landscape.</p></div>
    <div class="split__b prose">
      <p class="rv">FSA is pleased to introduce the FSA Development Program. The program connects students who have successfully secured internships with their peers, fostering mentorship and the exchange of proven strategies and resources.</p>
      <p class="rv">Participants will benefit from comprehensive guidance on résumé development, professional networking, interview preparation, and industry expectations. By equipping students with the essential skills and insights required to distinguish themselves in the job market, the Development Program aims to cultivate a pipeline of well-prepared candidates ready to pursue meaningful opportunities in finance!</p>
      <a class="btn btn--ink rv" href="join.html">Get access {ARROW}</a>
    </div>
  </div>
</section>
<section class="sec sec--ink">
  <div class="wrap">
    <div class="sec__head"><div><p class="kicker rv">Program overview</p><h2 class="rv">Five sessions. <em>Zero fluff.</em></h2></div></div>
    <ol class="syl syl--wide">{sessions}</ol>
  </div>
</section>
<section class="sec">
  <div class="wrap">
    <div class="sec__head"><div><p class="kicker rv">The team leads</p><h2 class="rv">Led by students who <em>landed it.</em></h2></div></div>
    <div class="people people--3">{leads}</div>
  </div>
</section>
<section class="sec sec--paper">
  <div class="wrap">
    <div class="sec__head"><div><p class="kicker rv">The mentors</p><h2 class="rv">In your <em>corner.</em></h2></div></div>
    <div class="people people--4">{mentors}</div>
  </div>
</section>
''' + foot()


def join():
    return head("Join FSA — Finance Students’ Association", "Become a member, apply for the Case Pool Team, or join the executive team.", "join") + page_hero(
        "Join FSA", "Get <em>in.</em>",
        "Invest in your future with a community that helps you grow faster than you can on your own.") + f'''
<section class="sec">
  <div class="wrap ways">
    <a class="way way--blue rv" href="{LINKTREE}" target="_blank" rel="noopener">
      <span class="idx">01</span><h2>General Membership</h2>
      <p>Get access to exclusive perks such as the FSA Development Program, the FSA WhatsApp Community, exclusive networking opportunities, the FSA Newsletter and more!</p>
      <span class="btn btn--acid">Become a member {ARROW}</span>
    </a>
    <a class="way way--ink rv" href="{LINKTREE}" target="_blank" rel="noopener">
      <span class="idx">02</span><h2>FSA Case Pool Team</h2>
      <p>Apply for the FSA Case Pool Team and gain hands-on experience in dealing with financials, modelling, networking with professionals, exclusive training sessions and access to various resources!</p>
      <span class="btn btn--bone">Apply now {ARROW}</span>
    </a>
    <div class="way way--soon rv">
      <span class="idx">03</span><h2>Executive Team</h2>
      <p>Interested in joining our executive team? The application form is coming soon.</p>
      <span class="chip chip--ink">Coming soon</span>
    </div>
  </div>
</section>
<section class="shot">
  <figure class="wrap rv"><img src="assets/events/session.jpg" alt="Students at an FSA session" loading="lazy" width="1280" height="304"><figcaption>An FSA session in progress.</figcaption></figure>
</section>
<section class="sec sec--paper">
  <div class="wrap split">
    <div class="split__a"><p class="kicker rv">Say hello</p><h2 class="rv">Questions? <em>Reach out.</em></h2></div>
    <div class="split__b contact">
      <a class="rv" href="mailto:{EMAIL}"><span>Email</span><b>{EMAIL}</b>{ARROW}</a>
      <a class="rv" href="{INSTAGRAM}" target="_blank" rel="noopener"><span>Instagram</span><b>@fsayorku</b>{ARROW}</a>
      <a class="rv" href="{LINKEDIN}" target="_blank" rel="noopener"><span>LinkedIn</span><b>Finance Students’ Association</b>{ARROW}</a>
    </div>
  </div>
</section>
''' + foot()


PAGES = {"index.html": home, "team.html": team, "advisors.html": advisors,
         "events.html": events, "program.html": program, "join.html": join}

if __name__ == "__main__":
    for name, fn in PAGES.items():
        (ROOT / name).write_text(fn(), encoding="utf-8")
        print("built", name)
