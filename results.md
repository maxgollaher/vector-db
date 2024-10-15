# Podcast Similarity Results

## Question 1 Query:

```sql

SELECT 
    p.title,
    ps.id,
    ps.content,
    ps.start_time,
    ps.end_time,
    ps.embedding <-> (SELECT embedding FROM podcast_segment WHERE id = '267:476' LIMIT 1) AS distance
FROM podcast_segment ps
JOIN podcast p ON ps.podcast_id = p.id
WHERE ps.id != '267:476'
ORDER BY distance ASC
LIMIT 5;

```
### Question 1 Results:
**Input:**  that if we were to meet alien life at some point

| Podcast Title                                                                                         | Segment ID   | Content                                                    |   Start Time |   End Time |   Distance |
|-------------------------------------------------------------------------------------------------------|--------------|------------------------------------------------------------|--------------|------------|------------|
| Ryan Graves: UFOs, Fighter Jets, and Aliens \| Lex Fridman Podcast #308                               | 113:2792     | encounters, human beings, if we were to meet another alien |      6725.62 |    6729.86 |   0.648345 |
| Richard Dawkins: Evolution, Intelligence, Simulation, and Memes \| Lex Fridman Podcast #87            | 268:1019     | Suppose we did meet an alien from outer space              |      2900.04 |    2903.08 |   0.655811 |
| Jeffrey Shainline: Neuromorphic Computing and Optoelectronic Intelligence \| Lex Fridman Podcast #225 | 305:3600     | but if we think of alien civilizations out there           |      9479.96 |    9484.04 |   0.659543 |
| Michio Kaku: Future of Humans, Aliens, Space Travel & Physics \| Lex Fridman Podcast #45              | 18:464       | So I think when we meet alien life from outer space,       |      1316.86 |    1319.58 |   0.666203 |
| Alien Debate: Sara Walker and Lee Cronin \| Lex Fridman Podcast #279                                  | 71:989       | because if aliens come to us                               |      2342.34 |    2343.62 |   0.674294 |

<div style="page-break-after: always;"></div>

## Question 2 Query:

```sql

SELECT 
    p.title,
    ps.id,
    ps.content,
    ps.start_time,
    ps.end_time,
    ps.embedding <-> (SELECT embedding FROM podcast_segment WHERE id = '267:476' LIMIT 1) AS distance
FROM podcast_segment ps
JOIN podcast p ON ps.podcast_id = p.id
WHERE ps.id != '267:476'
ORDER BY distance DESC
LIMIT 5;

```
### Question 2 Results:
**Input:**  that if we were to meet alien life at some point

| Podcast Title                                                                                      | Segment ID   | Content                                           |   Start Time |   End Time |   Distance |
|----------------------------------------------------------------------------------------------------|--------------|---------------------------------------------------|--------------|------------|------------|
| Jason Calacanis: Startups, Angel Investing, Capitalism, and Friendship \| Lex Fridman Podcast #161 | 119:218      | a 73 Mustang Grande in gold?                      |       519.96 |     523.8  |    1.61577 |
| Rana el Kaliouby: Emotion AI, Social Robots, and Self-Driving Cars \| Lex Fridman Podcast #322     | 133:2006     | for 94 car models.                                |      5818.62 |    5820.82 |    1.58634 |
| Travis Stevens: Judo, Olympics, and Mental Toughness \| Lex Fridman Podcast #223                   | 283:1488     | when I called down to get the sauna.              |      3709.34 |    3711.1  |    1.57255 |
| Jeremy Howard: fast.ai Deep Learning Courses and Research \| Lex Fridman Podcast #35               | 241:1436     | which has all the courses pre-installed.          |      4068.9  |    4071.14 |    1.56633 |
| Joscha Bach: Nature of Reality, Dreams, and Consciousness \| Lex Fridman Podcast #212              | 307:3933     | and very few are first class and some are budget. |     10648.6  |   10651    |    1.56163 |

<div style="page-break-after: always;"></div>

## Question 3 Query:

```sql

SELECT 
    p.title,
    ps.id,
    ps.content,
    ps.start_time,
    ps.end_time,
    ps.embedding <-> (SELECT embedding FROM podcast_segment WHERE id = '48:511' LIMIT 1) AS distance
FROM podcast_segment ps
JOIN podcast p ON ps.podcast_id = p.id
WHERE ps.id != '48:511'
ORDER BY distance ASC
LIMIT 5;

```
### Question 3 Results:
**Input:**  Is it is there something especially interesting and profound to you in terms of our current deep learning neural network, artificial neural network approaches and the whatever we do understand about the biological neural network.

| Podcast Title                                                                                      | Segment ID   | Content                                                                                                                                                                                                                                                    |   Start Time |   End Time |   Distance |
|----------------------------------------------------------------------------------------------------|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|------------|------------|
| Andrew Huberman: Neuroscience of Optimal Performance \| Lex Fridman Podcast #139                   | 155:648      | Is there something interesting to you or fundamental to you about the circuitry of the brain                                                                                                                                                               |      3798.48 |    3805.84 |   0.6523   |
| Cal Newport: Deep Work, Focus, Productivity, Email, and Social Media \| Lex Fridman Podcast #166   | 61:3707      | of what we might discover about neural networks?                                                                                                                                                                                                           |      8498.02 |    8500.1  |   0.712105 |
| Matt Botvinick: Neuroscience, Psychology, and AI at DeepMind \| Lex Fridman Podcast #106           | 48:512       | And our brain is there. There's some there's quite a few differences. Are some of them to you either interesting or perhaps profound in terms of in terms of the gap we might want to try to close in trying to create a human level intelligence.         |      1846.84 |    1865.84 |   0.71956  |
| Yann LeCun: Dark Matter of Intelligence and Self-Supervised Learning \| Lex Fridman Podcast #258   | 276:2642     | Have these, I mean, small pockets of beautiful complexity. Does that, do cellular automata, do these kinds of emergence and complex systems give you some intuition or guide your understanding of machine learning systems and neural networks and so on? |      8628.16 |    8646.16 |   0.735722 |
| Stephen Wolfram: Fundamental Theory of Physics, Life, and the Universe \| Lex Fridman Podcast #124 | 2:152        | So is there something like that with physics where so deep learning neural networks have been around for a long time?                                                                                                                                      |       610.86 |     618.86 |   0.736697 |

<div style="page-break-after: always;"></div>

## Question 4 Query:

```sql

SELECT 
    p.title,
    ps.id,
    ps.content,
    ps.start_time,
    ps.end_time,
    ps.embedding <-> (SELECT embedding FROM podcast_segment WHERE id = '51:56' LIMIT 1) AS distance
FROM podcast_segment ps
JOIN podcast p ON ps.podcast_id = p.id
WHERE ps.id != '51:56'
ORDER BY distance ASC
LIMIT 5;

```
### Question 4 Results:
**Input:**  But what about like the fundamental physics of dark energy? Is there any understanding of what the heck it is?

| Podcast Title                                                                                         | Segment ID   | Content                                                      |   Start Time |   End Time |   Distance |
|-------------------------------------------------------------------------------------------------------|--------------|--------------------------------------------------------------|--------------|------------|------------|
| George Hotz: Hacking the Simulation & Learning to Drive with Neural Nets \| Lex Fridman Podcast #132  | 308:144      | I mean, we don't understand dark energy, right?              |       500.44 |     502.6  |   0.668197 |
| Lex Fridman: Ask Me Anything - AMA January 2021 \| Lex Fridman Podcast                                | 243:273      | Like, what's up with this dark matter and dark energy stuff? |       946.22 |     950.12 |   0.735551 |
| Katherine de Kleer: Planets, Moons, Asteroids & Life in Our Solar System \| Lex Fridman Podcast #184  | 196:685      | being like, what the hell is dark matter and dark energy?    |      2591.72 |    2595.96 |   0.763114 |
| Alex Filippenko: Supernovae, Dark Energy, Aliens & the Expanding Universe \| Lex Fridman Podcast #137 | 51:36        | Do we have any understanding of what the heck that thing is? |       216    |     219    |   0.792202 |
| Leonard Susskind: Quantum Mechanics, String Theory and Black Holes \| Lex Fridman Podcast #41         | 122:831      | That is a big question in physics right now.                 |      2374.9  |    2377.62 |   0.80227  |

<div style="page-break-after: always;"></div>

## Question 5a Query:

```sql

SELECT 
    p.title,
    AVG(ps.embedding) <-> 
    (SELECT embedding FROM podcast_segment WHERE id = '267:476' LIMIT 1) AS distance
FROM podcast_segment ps
JOIN podcast p ON ps.podcast_id = p.id
WHERE p.id != (SELECT podcast_id FROM podcast_segment WHERE id = '267:476' LIMIT 1)
GROUP BY p.id, p.title
ORDER BY distance ASC
LIMIT 5;

```
### Question 5a Results:
**Input:**  that if we were to meet alien life at some point

| Podcast Title                                                                                   |   Average Distance |
|-------------------------------------------------------------------------------------------------|--------------------|
| Sara Walker: The Origin of Life on Earth and Alien Worlds \| Lex Fridman Podcast #198           |           0.782898 |
| Martin Rees: Black Holes, Alien Life, Dark Matter, and the Big Bang \| Lex Fridman Podcast #305 |           0.78795  |
| Max Tegmark: Life 3.0 \| Lex Fridman Podcast #1                                                 |           0.78869  |
| Sean Carroll: The Nature of the Universe, Life, and Intelligence \| Lex Fridman Podcast #26     |           0.789065 |
| Nick Bostrom: Simulation and Superintelligence \| Lex Fridman Podcast #83                       |           0.791121 |

<div style="page-break-after: always;"></div>

## Question 5b Query:

```sql

SELECT 
    p.title,
    AVG(ps.embedding) <-> 
    (SELECT embedding FROM podcast_segment WHERE id = '48:511' LIMIT 1) AS distance
FROM podcast_segment ps
JOIN podcast p ON ps.podcast_id = p.id
WHERE p.id != (SELECT podcast_id FROM podcast_segment WHERE id = '48:511' LIMIT 1)
GROUP BY p.id, p.title
ORDER BY distance ASC
LIMIT 5;

```
### Question 5b Results:
**Input:**  Is it is there something especially interesting and profound to you in terms of our current deep learning neural network, artificial neural network approaches and the whatever we do understand about the biological neural network.

| Podcast Title                                                                                   |   Average Distance |
|-------------------------------------------------------------------------------------------------|--------------------|
| Christof Koch: Consciousness \| Lex Fridman Podcast #2                                          |           0.75378  |
| Dileep George: Brain-Inspired AI \| Lex Fridman Podcast #115                                    |           0.760515 |
| Tomaso Poggio: Brains, Minds, and Machines \| Lex Fridman Podcast #13                           |           0.761555 |
| Elon Musk: Neuralink, AI, Autopilot, and the Pale Blue Dot \| Lex Fridman Podcast #49           |           0.776152 |
| Philip Goff: Consciousness, Panpsychism, and the Philosophy of Mind \| Lex Fridman Podcast #261 |           0.787206 |

<div style="page-break-after: always;"></div>

## Question 5c Query:

```sql

SELECT 
    p.title,
    AVG(ps.embedding) <-> 
    (SELECT embedding FROM podcast_segment WHERE id = '51:56' LIMIT 1) AS distance
FROM podcast_segment ps
JOIN podcast p ON ps.podcast_id = p.id
WHERE p.id != (SELECT podcast_id FROM podcast_segment WHERE id = '51:56' LIMIT 1)
GROUP BY p.id, p.title
ORDER BY distance ASC
LIMIT 5;

```
### Question 5c Results:
**Input:**  But what about like the fundamental physics of dark energy? Is there any understanding of what the heck it is?

| Podcast Title                                                                                      |   Average Distance |
|----------------------------------------------------------------------------------------------------|--------------------|
| Sean Carroll: Quantum Mechanics and the Many-Worlds Interpretation \| Lex Fridman Podcast #47      |           0.776714 |
| Stephen Wolfram: Fundamental Theory of Physics, Life, and the Universe \| Lex Fridman Podcast #124 |           0.808071 |
| Donald Hoffman: Reality is an Illusion - How Evolution Hid the Truth \| Lex Fridman Podcast #293   |           0.816583 |
| Cumrun Vafa: String Theory \| Lex Fridman Podcast #204                                             |           0.817347 |
| Avi Loeb: Aliens, Black Holes, and the Mystery of the Oumuamua \| Lex Fridman Podcast #154         |           0.825452 |

<div style="page-break-after: always;"></div>

## Question 6 Query:

```sql

SELECT
    p.title,
    AVG(ps.embedding) <-> (
        SELECT AVG(embedding)
        FROM podcast_segment
        WHERE podcast_id = 'VeH7qKZr0WI'
        LIMIT 1
    ) AS distance
FROM podcast_segment ps
JOIN podcast p ON ps.podcast_id = p.id
WHERE p.id != 'VeH7qKZr0WI'
GROUP BY p.id, p.title
ORDER BY distance ASC
LIMIT 5;

```
### Question 6 Results:
**Input:** Balaji Srinivasan: How to Fix Government, Twitter, Science, and the FDA | Lex Fridman Podcast #331

| Podcast Title                                                                                         |   Average Distance |
|-------------------------------------------------------------------------------------------------------|--------------------|
| Tyler Cowen: Economic Growth & the Fight Against Conformity & Mediocrity \| Lex Fridman Podcast #174  |           0.119501 |
| Eric Weinstein: Difficult Conversations, Freedom of Speech, and Physics \| Lex Fridman Podcast #163   |           0.125714 |
| Michael Malice and Yaron Brook: Ayn Rand, Human Nature, and Anarchy \| Lex Fridman Podcast #178       |           0.128427 |
| Steve Keen: Marxism, Capitalism, and Economics \| Lex Fridman Podcast #303                            |           0.129163 |
| Michael Malice: The White Pill, Freedom, Hope, and Happiness Amidst Chaos \| Lex Fridman Podcast #150 |           0.130409 |

<div style="page-break-after: always;"></div>

