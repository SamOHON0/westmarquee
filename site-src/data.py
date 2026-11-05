# West Marquees and Inflatables: site data
# Real images + copy sourced from westmarqueesandinflatables.ie

DOMAIN = "https://www.westmarqueesandinflatables.ie"
BUSINESS_ID = "cb395296-bd08-492a-a0fa-162f5fe5227b"
PARTYOPS = "https://partyops.app"
# Home-page availability calendar. PartyOps shows price_on_request items as
# available with "Price on request", so this works without prices loaded.
AVAILABILITY_CALENDAR = True
PHONE = "085 269 6628"
PHONE_INTL = "+353852696628"
EMAIL = "westmarqueesandinflatables@gmail.com"
WHATSAPP = "https://wa.me/353852696628?text=Hi%2C%20I%27d%20like%20to%20enquire%20about%20hire."
FACEBOOK = "https://www.facebook.com/people/West-Marquees-and-Inflatables/61552761500676/"
# Copies of the old WordPress uploads, kept in the repo so the photos survive
# the domain move off the old site.
IMG = "/assets/img/wp/"

PRODUCTS = [
    dict(slug="danger-zone-obstacle-course", name="Danger Zone Obstacle Course", cat="obstacle",
         tag="55ft", size="55ft (16.8m) long", ages="4+", img="/assets/img/danger-zone-obstacle-course.jpg",
         card="/assets/img/danger-zone-obstacle-course-card.jpg",  # 4:3 framing for cards and PartyOps
         gallery=["/assets/img/gallery/danger-zone-obstacle-course-1.jpg", "/assets/img/gallery/danger-zone-obstacle-course-2.jpg", "/assets/img/gallery/danger-zone-obstacle-course-3.jpg"],
         short="Our mammoth 55ft course with Climb Through Wall, Bish Bash Poles and a Giant Slide.",
         long="The Danger Zone is our flagship obstacle course and one of the biggest in the west of Ireland. Fifty five feet of climb through walls, bish bash poles, tunnels and a giant slide finish. It keeps a full party of kids moving for hours, and it photographs brilliantly at fun days, sports club events and big birthdays. Suitable for ages 4 and up."),
    dict(slug="military-assault-course", name="Military Assault Course", cat="obstacle",
         tag="55ft camo", size="55ft (16.8m) long", ages="4+", img="/assets/img/military-assault-course.jpg",
         card="/assets/img/military-assault-course-card.jpg",  # 4:3 framing for cards and PartyOps
         gallery=["/assets/img/gallery/military-assault-course-1.jpg", "/assets/img/gallery/military-assault-course-2.jpg", "/assets/img/gallery/military-assault-course-3.jpg"],
         short="A 55ft camouflage assault course with tunnels, rope climb, bish bash poles and a giant slide.",
         long="Full camouflage colours and a proper army feel. The Military Assault Course runs 55ft with tunnels, a rope climb, bish bash poles and a giant slide at the end. A favourite for school fun days and communions where you have a crowd of kids to wear out. Ages 4 and up."),
    dict(slug="drop-zone-obstacle-course", name="Drop Zone Obstacle Course", cat="obstacle",
         tag="52ft, ages 10+", size="52ft x 15ft", ages="10+", img="/assets/img/drop-zone-obstacle-course.jpg",
         card="/assets/img/drop-zone-obstacle-course-card.jpg",  # 4:3 framing for cards and PartyOps
         gallery=["/assets/img/gallery/drop-zone-obstacle-course-1.jpg", "/assets/img/gallery/drop-zone-obstacle-course-2.jpg", "/assets/img/gallery/drop-zone-obstacle-course-3.jpg"],
         short="A massive 52ft x 15ft course with climbing blocks, roller bars, hangers and a jump pad.",
         long="Built for older kids who find the standard castles too tame. The Drop Zone is 52ft by 15ft of climbing blocks, roller bars, hangers and a jump pad. Ideal for confirmations, teen birthdays and club events where you need something with a bit more challenge. Ages 10 and up."),
    dict(slug="disco-obstacle-course", name="Disco Obstacle Course", cat="obstacle",
         tag="Most popular", size="44ft long", ages="2 to 14", img="/assets/img/disco-obstacle-course.jpg",
         card="/assets/img/disco-obstacle-course-card.jpg",  # 4:3 framing for cards and PartyOps
         gallery=["/assets/img/gallery/disco-obstacle-course-1.jpg", "/assets/img/gallery/disco-obstacle-course-2.jpg", "/assets/img/gallery/disco-obstacle-course-3.jpg"],
         short="Our most popular 44ft course, packed with tunnels, bish bash, climb walls and a big slide.",
         long="Our most requested unit, and for good reason. The Disco course packs tunnels, bish bash obstacles, climb walls and a big slide into 44ft, and it suits everyone from age 2 up to 14. With over 40 themes available there is a version for every party."),
    dict(slug="crazy-croc-obstacle-course", name="Crazy Croc Obstacle Course", cat="obstacle",
         tag="New", size="45ft x 10ft, 8ft slide", ages="Ask us", img="/assets/img/crazy-croc-obstacle-course.jpg",
         card="/assets/img/crazy-croc-obstacle-course-card.jpg",  # 4:3 framing for cards and PartyOps
         gallery=["/assets/img/gallery/crazy-croc-obstacle-course-1.jpg", "/assets/img/gallery/crazy-croc-obstacle-course-2.jpg", "/assets/img/gallery/crazy-croc-obstacle-course-3.jpg"],
         short="A 45ft crocodile course: in through the jaws, over the obstacles and down an 8ft slide.",
         long="Brand new for this season. The Crazy Croc is 45ft by 10ft, and kids run in through the crocodile's jaws, push through the pop-up obstacles and tunnels, then climb up and over the 8ft slide. Bright, colourful and a real head turner at birthdays, communions and school fun days. Competitively priced, contact us for a quote."),
    dict(slug="power-up-obstacle-course", name="Power-Up Obstacle Course", cat="obstacle",
         tag="New", size="40ft x 10ft, 7ft slide", ages="Ask us", img="/assets/img/power-up-obstacle-course.jpg",
         card="/assets/img/power-up-obstacle-course-card.jpg",  # 4:3 framing for cards and PartyOps
         gallery=["/assets/img/gallery/power-up-obstacle-course-1.jpg", "/assets/img/gallery/power-up-obstacle-course-2.jpg"],
         short="A 40ft gamer-themed course with pop-up obstacles, a climb wall and a 7ft slide.",
         long="Brand new for this season and made for gamers. The Power-Up course is 40ft by 10ft in neon controller graphics, with pop-up obstacles, a climbing wall and a 7ft slide to finish. A great fit for birthdays where the kids would normally be glued to a console. Competitively priced, contact us for a quote."),
    dict(slug="active-adventure-obstacle-course", name="Active Adventure Obstacle Course", cat="obstacle",
         tag="New", size="45ft x 10ft, 8ft slide", ages="Ask us", img="/assets/img/active-adventure-obstacle-course.jpg",
         card="/assets/img/active-adventure-obstacle-course-card.jpg",  # 4:3 framing for cards and PartyOps
         gallery=["/assets/img/gallery/active-adventure-obstacle-course-1.jpg", "/assets/img/gallery/active-adventure-obstacle-course-2.jpg", "/assets/img/gallery/active-adventure-obstacle-course-3.jpg", "/assets/img/gallery/active-adventure-obstacle-course-4.jpg"],
         short="A colourful 45ft course with tunnels, pop-up obstacles and an 8ft slide.",
         long="Brand new for this season. The Active Adventure course is 45ft by 10ft of tunnels, pop-up obstacles and a climb up to an 8ft slide, all in bright party colours. Ideal for birthdays, communions, school sports days and club fun days. Competitively priced, contact us for a quote."),
    dict(slug="prison-break-obstacle-course", name="Prison Break Obstacle Course", cat="obstacle",
         tag="New", size="Ask us", ages="Ask us", img="/assets/img/prison-break-obstacle-course.jpg",
         card="/assets/img/prison-break-obstacle-course-card.jpg",  # 4:3 framing for cards and PartyOps
         gallery=["/assets/img/gallery/prison-break-obstacle-course-1.jpg", "/assets/img/gallery/prison-break-obstacle-course-2.jpg", "/assets/img/gallery/prison-break-obstacle-course-3.jpg"],
         short="Break out of the jailhouse: in through the prison gates, past the obstacles and down the slide.",
         long="Brand new for this season. The Prison Break course has a stone-walled jailhouse front with twin arched gates, then pop-up obstacles and a run of bump-through pillars before the climb up to the slide. A great pick for birthdays, communions and school fun days. Competitively priced, contact us for a quote."),
    dict(slug="combi-castle-princess", name="Combi Castle: Princess", cat="castle",
         tag="3D Princess", size="16ft x 15ft", ages="2+", img="2026/05/combi-bouncy-castles-for-hire.png",
         short="Spacious bouncing area, a slide and a huge 3D Princess attachment.",
         long="A spacious bouncing area, a slide and a 3D Princess attachment on top. 16ft by 15ft. One of our most requested units for birthdays and communions."),
    dict(slug="combi-castle-barbie", name="Combi Castle: Barbie", cat="castle",
         tag="Themed", size="16ft x 15ft", ages="2+", img="/assets/img/combi-castle-barbie.jpg",
         card="/assets/img/combi-castle-barbie-card.jpg",  # 4:3 framing for cards and PartyOps
         gallery=["/assets/img/gallery/combi-castle-barbie-1.jpg", "/assets/img/gallery/combi-castle-barbie-2.jpg"],
         short="Bright pink Barbie themed combi with bouncing area and slide.",
         long="Bright pink and impossible to miss. The Barbie combi has a full bouncing area plus a slide, at 16ft by 15ft. It books out fast in summer, so get your date in early."),
    dict(slug="combi-castle-paw-patrol", name="Combi Castle: Paw Patrol", cat="castle",
         tag="Themed", size="16ft x 15ft", ages="2+", img="2026/05/combi-bouncy-castles-for-hire.png",
         short="Paw Patrol themed combi with bouncing area and slide.",
         long="A guaranteed hit for younger kids. The Paw Patrol combi pairs a roomy bouncing area with a slide, at 16ft by 15ft. Perfect for preschool birthdays and family days."),
    dict(slug="combi-castle-spiderman", name="Combi Castle: Spiderman", cat="castle",
         tag="Themed", size="16ft x 15ft", ages="2+", img="2026/05/combi-bouncy-castles-for-hire.png",
         short="Spiderman themed combi with bouncing area and slide.",
         long="Superhero vibes all day. The Spiderman combi has a full bouncing area and slide at 16ft by 15ft, and it suits boys and girls from toddlers up."),
    dict(slug="double-the-fun-castle", name="Double the Fun Castle", cat="castle",
         tag="Party ready", size="Ask us", ages="2+", img="2026/04/DOUBLE-THE-FUN-1-1024x929.png",
         short="A vibrant rainbow-coloured bouncy castle with slide.",
         long="A vibrant rainbow coloured bouncy castle with a slide and eye catching themes. The Double the Fun castle is the classic garden party pick: bright, roomy and loved by every age group at the party."),
    dict(slug="marquee-hire", name="Marquee Hire", cat="marquee",
         tag="Any event", size="Sized to your event", ages="Everyone", img="/assets/img/marquee-hire.jpg",
         card="/assets/img/marquee-hire-card.jpg",  # 4:3 framing for cards and PartyOps
         gallery=["/assets/img/gallery/marquee-hire-1.jpg", "/assets/img/gallery/marquee-hire-2.jpg", "/assets/img/gallery/marquee-hire-3.jpg", IMG + "2026/04/marquees-galway-for-hire-rent.jpg"],
         short="Clean, spacious marquees for weddings, communions, birthdays and corporate events.",
         long="Clean, spacious marquees professionally set up by our team. We supply marquees for weddings, communions, birthdays, corporate events and everything in between, across the west of Ireland. Fitted out with dining tables and chairs, or cocktail tables and stools, in whatever layout suits the day, and they can be hired together with our inflatables. Tell us your numbers and your venue and we will recommend the right size."),
    dict(slug="pub-inflatable", name="The Pub Inflatable", cat="pub",
         tag="Signature", size="Ask us", ages="Adults", img="2026/05/pub-home.jpg",
         short="Styled like a traditional Irish pub outside, marquee-style inside.",
         long="Styled like a traditional Irish pub on the outside and marquee style on the inside. Used as a bar area, a seating space or the centrepiece of the event at weddings, festivals, birthdays and garden parties. One of very few in Ireland."),
    dict(slug="foot-dart-board", name="4M Foot Dart Board", cat="games",
         tag="4 metres", size="4m board", ages="6+", img="2026/04/home-foot-dart-board.jpg",
         short="Football meets darts on a giant 4 metre board.",
         long="Football meets darts on a giant 4 metre inflatable board. Kick the velcro footballs and aim for a perfect 180. Brilliant for communions, confirmations, birthdays and corporate days, and it works for all ages and abilities."),
    dict(slug="penalty-shootout", name="Penalty Shootout", cat="games",
         tag="New", size="Ask us", ages="All ages", img="/assets/img/penalty-shootout.jpg",
         short="An inflatable goal with a diving keeper and scoring targets: pick your corner and beat him.",
         long="The newest addition to our games range. The inflatable Penalty Shootout gives everyone a go at scoring the winning penalty, from small kids to the grown ups who think they still have it. A great crowd puller at communions, birthdays, GAA and soccer club fun days and corporate events, and it pairs perfectly with the Foot Dart Board. Competitively priced, contact us for a quote."),
]

CATS = dict(
    obstacle="Obstacle Courses",
    castle="Combi Castles",
    marquee="Marquees",
    pub="Pub Inflatable",
    games="Games",
)

COUNTIES = [
    dict(slug="galway", name="Galway", towns=["Galway City", "Oranmore", "Athenry", "Tuam", "Loughrea", "Gort", "Claregalway", "Barna", "Moycullen", "Headford"]),
    dict(slug="mayo", name="Mayo", towns=["Castlebar", "Westport", "Ballina", "Claremorris", "Ballinrobe", "Swinford", "Kiltimagh"]),
    dict(slug="roscommon", name="Roscommon", towns=["Roscommon Town", "Boyle", "Castlerea", "Ballaghaderreen", "Strokestown", "Athleague"]),
    dict(slug="clare", name="Clare", towns=["Ennis", "Shannon", "Ennistymon", "Kilrush", "Sixmilebridge", "Newmarket-on-Fergus"]),
    dict(slug="limerick", name="Limerick", towns=["Limerick City", "Newcastle West", "Adare", "Annacotty", "Castletroy", "Caherdavin"]),
]

TOWNS = [
    dict(slug="galway-city", name="Galway City", county="Galway"),
    dict(slug="oranmore", name="Oranmore", county="Galway"),
    dict(slug="athenry", name="Athenry", county="Galway"),
    dict(slug="tuam", name="Tuam", county="Galway"),
    dict(slug="loughrea", name="Loughrea", county="Galway"),
    dict(slug="castlebar", name="Castlebar", county="Mayo"),
    dict(slug="westport", name="Westport", county="Mayo"),
    dict(slug="ballina", name="Ballina", county="Mayo"),
    dict(slug="roscommon-town", name="Roscommon Town", county="Roscommon"),
    dict(slug="ennis", name="Ennis", county="Clare"),
    dict(slug="limerick-city", name="Limerick City", county="Limerick"),
]

# Area page copy. Facts only: product details come from PRODUCTS above, drive
# figures from DRIVE below. No prices, no claims about local popularity, and
# only the places Hugh lists in COUNTIES. Plain ASCII (the build writes with
# the system encoding).
AREA_COPY = {
    # ------------------------------------------------------------- counties --
    "galway": dict(
        img=IMG + "2026/04/home-danger-zone.jpg", img_alt="Danger Zone obstacle course",
        focus_h="One party, every age",
        focus="When the guest list runs from toddlers to grandparents, these three between them cover everyone: a course the youngest can manage, a bigger one for a crowd, and somewhere for the adults to sit.",
        picks=[
            ("disco-obstacle-course", "our most requested unit, with tunnels, bish bash obstacles, climb walls and a big slide, and over 40 themes to choose from."),
            ("danger-zone-obstacle-course", "our flagship course, with climb through walls, bish bash poles, tunnels and a giant slide finish, built to keep a full party of kids moving for hours."),
            ("marquee-hire", "fitted out with dining tables and chairs, or cocktail tables and stools, and it can be hired together with any of the inflatables."),
        ],
        faqs=[
            ("Can I book a marquee and an inflatable together?",
             "Yes. Marquees can be hired together with our inflatables and are set up by the same team. Tell us your guest numbers and your venue and we will recommend the right marquee size."),
        ]),
    "mayo": dict(
        img="/assets/img/prison-break-obstacle-course.jpg", img_alt="Prison Break obstacle course",
        focus_h="New courses this season",
        focus="Four of our obstacle courses are brand new for this season, and these are three of them. Each one has a different theme, so you can pick the one that suits the birthday child or the occasion.",
        picks=[
            ("crazy-croc-obstacle-course", "kids run in through the crocodile's jaws, push through the pop-up obstacles and tunnels, then climb up and over the 8ft slide."),
            ("prison-break-obstacle-course", "a stone-walled jailhouse front with twin arched gates, then pop-up obstacles and bump-through pillars before the climb up to the slide."),
            ("active-adventure-obstacle-course", "tunnels, pop-up obstacles and a climb up to an 8ft slide in bright party colours, suited to birthdays, communions, school sports days and club fun days."),
        ],
        faqs=[
            ("What is new in the range this season?",
             "Four obstacle courses are brand new this season: the Crazy Croc, Power-Up, Active Adventure and Prison Break. The Penalty Shootout is the newest addition to our games."),
        ]),
    "roscommon": dict(
        img=IMG + "2026/04/home-foot-dart-board.jpg", img_alt="4M Foot Dart Board",
        focus_h="Communions and confirmations",
        focus="A communion usually means younger children and a confirmation means older ones, so the right unit is different for each. These three cover both, with a game the adults will join in on too.",
        picks=[
            ("combi-castle-princess", "a spacious bouncing area, a slide and a 3D Princess attachment on top, and one of our most requested units for birthdays and communions."),
            ("drop-zone-obstacle-course", "climbing blocks, roller bars, hangers and a jump pad, built for older kids who find the standard castles too tame."),
            ("foot-dart-board", "kick velcro footballs at a giant 4 metre board and aim for a perfect 180. It works for all ages and abilities."),
        ],
        faqs=[
            ("What suits a confirmation?",
             "The Drop Zone Obstacle Course is for ages 10 and up and is ideal for confirmations, teen birthdays and club events. The 4M Foot Dart Board and the Penalty Shootout work for all ages, so the adults can play as well."),
        ]),
    "clare": dict(
        img=IMG + "2026/04/home-dropzone.jpg", img_alt="Drop Zone obstacle course",
        focus_h="If you have the space: our three biggest courses",
        focus="Our three largest listed courses all run over 50ft. They suit a big garden, a field or a school or club ground, and they keep a large group of children busy at once.",
        picks=[
            ("danger-zone-obstacle-course", "climb through walls, bish bash poles, tunnels and a giant slide finish, and one of the biggest courses in the west of Ireland."),
            ("military-assault-course", "full camouflage colours with tunnels, a rope climb, bish bash poles and a giant slide at the end."),
            ("drop-zone-obstacle-course", "climbing blocks, roller bars, hangers and a jump pad for older kids who want more of a challenge."),
        ],
        faqs=[
            ("How much space do the big courses need?",
             "The Danger Zone and Military Assault Course are 55ft long and the Drop Zone is 52ft by 15ft. Add at least 1.5 metres of clear space on every side, so allow roughly 65ft of flat length for the 55ft courses and about 62ft by 25ft for the Drop Zone. If you are not sure, send us a photo on WhatsApp."),
        ]),
    "limerick": dict(
        img=IMG + "2026/04/marquees-galway-for-hire-rent.jpg", img_alt="Marquee set up by West Marquees",
        focus_h="Work and corporate events",
        focus="For a staff day or a company event the adults are the main guests, so the marquee and the games matter more than the castles. All three are delivered and set up by our team.",
        picks=[
            ("marquee-hire", "supplied for corporate events as well as weddings and family occasions, laid out with dining tables and chairs or cocktail tables and stools."),
            ("foot-dart-board", "football meets darts on a giant 4 metre board, and it works for all ages and abilities."),
            ("penalty-shootout", "an inflatable goal with a diving keeper and scoring targets, so everyone gets a go at the winning penalty."),
        ],
        faqs=[
            ("Do you supply work and corporate events?",
             "Yes. We supply marquees for corporate events, and the 4M Foot Dart Board and the Penalty Shootout are both suited to corporate days. Tell us your numbers and venue and we will recommend a setup."),
        ]),
    # ---------------------------------------------------------------- towns --
    "galway-city": dict(
        img=IMG + "2026/05/combi-bouncy-castles-for-hire.png", img_alt="Combi bouncy castle",
        focus_h="Units for a smaller garden",
        focus="If your garden is on the small side, the footprint matters more than anything else. Every unit needs at least 1.5 metres of clear space on all sides, so these are the ones to look at first.",
        picks=[
            ("combi-castle-paw-patrol", "a roomy bouncing area with a slide, and a good fit for preschool birthdays."),
            ("combi-castle-barbie", "bright pink and impossible to miss, with a full bouncing area plus a slide."),
            ("power-up-obstacle-course", "the shortest of our courses with a listed size, in neon controller graphics with pop-up obstacles and a climbing wall."),
        ],
        faqs=[
            ("Which units fit a small garden?",
             "The combi castles are 16ft by 15ft, so with the 1.5 metre clearance they need roughly 26ft by 25ft of flat ground. The Power-Up course is 40ft by 10ft, needing roughly 50ft by 20ft. Send us a photo of your garden on WhatsApp and we will tell you what fits."),
        ]),
    "oranmore": dict(
        drive_h="Our home base",
        img="/assets/img/bundle-the-fun.jpg", img_alt="Penalty Shootout and Giant Foot Darts, added to an obstacle course booking",
        focus_h="Bundle the fun",
        focus="Booking an obstacle course? You can add an inflatable game to the same booking, delivered and set up with your course on the day, and give the grown ups something to queue for too.",
        picks=[
            ("crazy-croc-obstacle-course", "brand new this season: in through the crocodile's jaws, through the pop-up obstacles and tunnels and down the 8ft slide."),
            ("penalty-shootout", "an inflatable goal with a diving keeper, for small kids and for the grown ups who think they still have it."),
            ("foot-dart-board", "kick the velcro footballs at a 4 metre board and aim for a 180. It pairs well with the Penalty Shootout."),
        ],
        faqs=[
            ("Can I add a game to an obstacle course booking?",
             "Yes. When you book an obstacle course you can add the Penalty Shootout or the Giant Foot Darts, and we deliver and set it up with your course on the day. Ask us about a bundle when you book."),
        ]),
    "athenry": dict(
        img=IMG + "2026/04/home-military-assault-obstacle-course.jpg", img_alt="Military Assault obstacle course",
        focus_h="Planning a communion",
        focus="A communion day often means a crowd of children and plenty of adults at the same time. A castle or course for the kids and a marquee for everyone else covers both.",
        picks=[
            ("combi-castle-princess", "a bouncing area, a slide and a 3D Princess attachment, and one of our most requested units for birthdays and communions."),
            ("military-assault-course", "tunnels, a rope climb, bish bash poles and a giant slide, and a favourite for communions where you have a crowd of kids to wear out."),
            ("marquee-hire", "set up by our team with dining tables and chairs or cocktail tables and stools, and it can be hired together with either inflatable."),
        ],
        faqs=[
            ("Can we have a marquee for the adults and a castle for the kids?",
             "Yes. Marquees can be hired together with any of our inflatables and are set up by the same team. Tell us your guest numbers and we will recommend the right size."),
        ]),
    "tuam": dict(
        img=IMG + "2026/05/Disco-Home.png", img_alt="Disco obstacle course",
        focus_h="Parties for younger children",
        focus="For a party of under tens, a themed castle or a course with a low age limit is the safe choice. All three of these suit children from age 2.",
        picks=[
            ("disco-obstacle-course", "tunnels, bish bash obstacles, climb walls and a big slide, suited to everyone from age 2 up to 14, with over 40 themes."),
            ("combi-castle-spiderman", "a full bouncing area and slide, and it suits boys and girls from toddlers up."),
            ("combi-castle-barbie", "bright pink with a full bouncing area plus a slide. It books out fast in summer, so get your date in early."),
        ],
        faqs=[
            ("What ages is the Disco obstacle course for?",
             "The Disco course suits children from age 2 up to 14. It is 44ft long, and with over 40 themes available there is a version for most party themes."),
        ]),
    "loughrea": dict(
        img=IMG + "2026/04/home-dropzone.jpg", img_alt="Drop Zone obstacle course",
        focus_h="For older kids and teens",
        focus="Older children can find a standard bouncy castle too tame. These three give them a proper challenge or a game to compete at.",
        picks=[
            ("drop-zone-obstacle-course", "climbing blocks, roller bars, hangers and a jump pad, built for confirmations, teen birthdays and club events."),
            ("penalty-shootout", "an inflatable goal with a diving keeper and scoring targets: pick your corner and beat him."),
            ("foot-dart-board", "football meets darts on a giant 4 metre board, a good one for confirmations and for teenagers who want to compete."),
        ],
        faqs=[
            ("What do you have for kids who are too old for a bouncy castle?",
             "The Drop Zone Obstacle Course is for ages 10 and up, with climbing blocks, roller bars, hangers and a jump pad. The Penalty Shootout is for all ages and the 4M Foot Dart Board for ages 6 and up, so teenagers and adults can play too."),
        ]),
    "castlebar": dict(
        img=IMG + "2026/04/marquees-galway-for-hire-rent.jpg", img_alt="Marquee set up by West Marquees",
        focus_h="A marquee and a castle together",
        focus="For a family event, a marquee gives the adults somewhere to sit whatever the weather, while the children have the castle. Add a game and there is something for every age.",
        picks=[
            ("marquee-hire", "clean and spacious, set up by our team, and fitted out with dining tables and chairs or cocktail tables and stools."),
            ("combi-castle-paw-patrol", "a roomy bouncing area with a slide, and a good fit for preschool birthdays and family days."),
            ("foot-dart-board", "kick the velcro footballs and aim for a perfect 180. It suits communions, confirmations and birthdays, and works for all ages and abilities."),
        ],
        faqs=[
            ("What can go inside the marquee?",
             "We fit marquees out with dining tables and chairs, or cocktail tables and stools, in whatever layout suits the day. Tell us your numbers and your venue and we will recommend the right size."),
        ]),
    "westport": dict(
        img=IMG + "2026/05/pub-home.jpg", img_alt="The Pub Inflatable",
        focus_h="Weddings and garden parties",
        focus="For an adult event, the Pub Inflatable and a marquee do the heavy lifting, and a classic castle keeps any children at the party busy.",
        picks=[
            ("pub-inflatable", "styled like a traditional Irish pub on the outside and marquee style on the inside, used as a bar area, seating space or centrepiece."),
            ("marquee-hire", "supplied for weddings and set up by our team, and it can be hired together with the Pub Inflatable."),
            ("double-the-fun-castle", "a bright rainbow castle with a slide, and the classic garden party pick, loved by every age group."),
        ],
        faqs=[
            ("What is the Pub Inflatable?",
             "It is an inflatable styled like a traditional Irish pub on the outside and marquee style on the inside. People use it as a bar area, a seating space or the centrepiece of the event at weddings, festivals, birthdays and garden parties. It is one of very few in Ireland."),
        ]),
    "ballina": dict(
        img="/assets/img/danger-zone-obstacle-course.jpg", img_alt="Danger Zone obstacle course",
        focus_h="School and club fun days",
        focus="At a fun day you have a large group of children and a fixed amount of time. A long obstacle course moves them through quickly, and a game gives parents and coaches a go too.",
        picks=[
            ("danger-zone-obstacle-course", "our flagship course, and a good fit for fun days and sports club events."),
            ("military-assault-course", "tunnels, a rope climb, bish bash poles and a giant slide, and a favourite for school fun days."),
            ("penalty-shootout", "a crowd puller at GAA and soccer club fun days, for small kids and grown ups alike."),
        ],
        faqs=[
            ("Which units suit a school or club fun day?",
             "The Danger Zone and the Military Assault Course are both 55ft long and suited to large groups of children. The Penalty Shootout suits GAA and soccer club fun days, and pairs with the 4M Foot Dart Board."),
        ]),
    "roscommon-town": dict(
        img="/assets/img/active-adventure-obstacle-course.jpg", img_alt="Active Adventure obstacle course",
        focus_h="Birthdays and communions",
        focus="For a birthday or a communion, a colourful course or a themed castle is the usual choice. Two of these are new this season, and the third suits younger children.",
        picks=[
            ("active-adventure-obstacle-course", "brand new this season, with tunnels, pop-up obstacles and an 8ft slide in bright party colours."),
            ("prison-break-obstacle-course", "brand new this season: in through the prison gates, past the obstacles and bump-through pillars and down the slide."),
            ("combi-castle-spiderman", "a full bouncing area and slide that suits boys and girls from toddlers up."),
        ],
        faqs=[
            ("Can I hire for a full weekend?",
             "Yes. We offer day, midweek and weekend hire. Tell us your dates when you send your booking request and we will confirm what is available."),
        ]),
    "ennis": dict(
        img="/assets/img/crazy-croc-obstacle-course.jpg", img_alt="Crazy Croc obstacle course",
        focus_h="Obstacle course or bouncy castle?",
        focus="A castle gives children a bouncing area and a slide in a compact space. A course gives them a run of obstacles from start to finish but needs more length. Here is one of each, plus one in between.",
        picks=[
            ("double-the-fun-castle", "a rainbow coloured castle with a slide, the classic garden party pick."),
            ("disco-obstacle-course", "a 44ft course with tunnels, bish bash obstacles, climb walls and a big slide, for ages 2 to 14."),
            ("crazy-croc-obstacle-course", "in through the crocodile's jaws, through pop-up obstacles and tunnels and over an 8ft slide."),
        ],
        faqs=[
            ("Should I get an obstacle course or a castle?",
             "It mostly depends on your space and the ages. Our combi castles are 16ft by 15ft and suit ages 2 and up. Our courses with a listed size run from 40ft to 55ft long and keep a bigger group moving. Send us a photo of your space on WhatsApp and we will tell you what fits."),
        ]),
    "limerick-city": dict(
        img=IMG + "2026/05/pub-home.jpg", img_alt="The Pub Inflatable",
        focus_h="Something different",
        focus="If you want something guests will not have seen at every other party, these are the units to look at.",
        picks=[
            ("pub-inflatable", "a traditional Irish pub outside and marquee style inside, and one of very few in Ireland."),
            ("drop-zone-obstacle-course", "52ft of climbing blocks, roller bars, hangers and a jump pad for older kids who find standard castles too tame."),
            ("prison-break-obstacle-course", "brand new this season, with a stone-walled jailhouse front, twin arched gates and bump-through pillars."),
        ],
        faqs=[
            ("Do you have anything for adults?",
             "Yes. The Pub Inflatable is aimed at adults and works as a bar area, seating space or centrepiece. The Penalty Shootout and the 4M Foot Dart Board are for all ages, grown ups included, and we supply marquees too."),
        ]),
}


# Road distance and drive time from Oranmore to each listed place, measured
# 5 Nov 2026 with OSRM (router.project-osrm.org) on OpenStreetMap data,
# town centres geocoded with Photon (OSM). km rounded to whole km, minutes to
# the nearest 5. Real times vary with traffic and towing.
DRIVE = {
    "Galway City": dict(km=12, mins=15),
    "Oranmore": dict(km=0, mins=0),
    "Athenry": dict(km=13, mins=15),
    "Tuam": dict(km=39, mins=30, via="M17"),
    "Loughrea": dict(km=27, mins=25),
    "Gort": dict(km=27, mins=20),
    "Headford": dict(km=32, mins=30),
    "Castlebar": dict(km=94, mins=75, via="M17 and N17"),
    "Westport": dict(km=86, mins=80, via="N84"),
    "Ballina": dict(km=118, mins=100, via="M17 and N17"),
    "Claremorris": dict(km=66, mins=50),
    "Ballinrobe": dict(km=54, mins=50),
    "Swinford": dict(km=96, mins=75),
    "Kiltimagh": dict(km=84, mins=65),
    "Roscommon Town": dict(km=80, mins=70, via="N63"),
    "Boyle": dict(km=110, mins=95),
    "Castlerea": dict(km=83, mins=70),
    "Ballaghaderreen": dict(km=95, mins=80),
    "Strokestown": dict(km=100, mins=90),
    "Athleague": dict(km=71, mins=60),
    "Ennis": dict(km=55, mins=45, via="M18"),
    "Shannon": dict(km=70, mins=50),
    "Kilrush": dict(km=100, mins=80),
    "Sixmilebridge": dict(km=76, mins=55),
    "Newmarket-on-Fergus": dict(km=63, mins=45),
    "Limerick City": dict(km=88, mins=65, via="M18"),
    "Newcastle West": dict(km=129, mins=95),
    "Adare": dict(km=105, mins=75),
    "Annacotty": dict(km=100, mins=70),
    "Castletroy": dict(km=95, mins=70),
    "Caherdavin": dict(km=86, mins=65),
    "Claregalway": dict(km=9, mins=10),
    "Barna": dict(km=20, mins=25),
    "Moycullen": dict(km=23, mins=25),
    "Ennistymon": dict(km=65, mins=65),
}

REVIEWS = [
    dict(stars=5, text="Hired the Danger Zone for our lad's 10th and it was a massive hit. Spotless setup and the team were a pleasure to deal with.", who="Aoife M.", where="Galway City"),
    dict(stars=5, text="Got a marquee and the Princess combi for a communion. Great value together and setup was seamless. Would book again in a heartbeat.", who="Ciara D.", where="Castlebar"),
    dict(stars=5, text="The Pub Inflatable was the talk of the party. Something a bit different and everyone was raving about it. Punctual and clean.", who="Declan H.", where="Roscommon"),
]

FAQS = [
    ("What can I hire?",
     "A wide range of inflatables and event hire: 55ft obstacle courses (Danger Zone, Military Assault, Drop Zone), the Disco obstacle course, our new Crazy Croc, Power-Up, Active Adventure and Prison Break courses, combi bouncy castles in Princess, Barbie, Paw Patrol and Spiderman themes, the 4M Foot Dart Board, the Penalty Shootout, marquees and the unique Pub Inflatable."),
    ("What areas do you cover?",
     "We cover the west of Ireland: Galway, Mayo, Roscommon, Clare and Limerick. Based in Oranmore, Co Galway, we regularly serve Galway City, Athenry, Tuam, Loughrea, Castlebar, Westport, Ballina, Roscommon town, Ennis and Limerick City."),
    ("How do I book?",
     "Use the Book Online page to pick your item and date and send a booking request. We confirm availability and price by phone or email, usually the same day. You can also call or WhatsApp us on 085 269 6628."),
    ("Are your inflatables safe?",
     "Yes. We are fully insured for inflatable hire and every unit is cleaned and inspected between hires. Safety, reliability and professionalism are at the heart of everything we do."),
    ("What do I need for setup?",
     "A flat area big enough for the unit with at least 1.5 metres of clear space on all sides, clear access to the site, and a standard plug socket nearby for the blower. If you are unsure about your space, send us a photo on WhatsApp and we will tell you straight away."),
    ("Can I hire a party package?",
     "Yes. We offer day, midweek and weekend hire, and we are happy to build a package. Combine an obstacle course with a combi castle, add the Foot Dart Board or Penalty Shootout to an obstacle course for as little as €100 extra, or pair a marquee with the Pub Inflatable."),
    ("What happens if it rains?",
     "Most of our castles have rain covers and light rain is no problem. In high winds or severe weather we will work with you to rearrange, we never leave you stuck."),
]
