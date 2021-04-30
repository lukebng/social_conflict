from otree.api import *
from otree.models import player

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'showup'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


def make_likert_7(label):
    return models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label=label,
        widget=widgets.RadioSelectHorizontal,
    )


class Group(BaseGroup):
    pass


class Player(BasePlayer):
        amb1 = make_likert_7("")
        amb2 = make_likert_7("")
        amb3 = make_likert_7("")
        amb4 = make_likert_7("")
        amb5 = make_likert_7("")
        amb6 = make_likert_7("")
        amb7 = make_likert_7("")
        amb8 = make_likert_7("")
        amb9 = make_likert_7("")
        amb10 = make_likert_7("")

#Functions
def custom_export(players):
    # header row
    yield ['DLCID', 'ambv1', 'ambv2', 'ambv3', 'ambv4', 'ambv5', 'ambv6', 'ambv7', 'ambv8', 'ambv9', 'ambv10',
           'payoff', 'sessionid', 'group']
    for p in players:
        participant = p.participant
        session = p.session
        yield [participant.label, p.amb1, p.amb2, p.amb3, p.amb4, p.amb5, p.amb6, p.amb7, p.amb8, p.amb9, p.amb10,
               p.payoff, session, p.group]

# PAGES
class Showup(Page):

    def vars_for_template(player: Player):
        return dict(role=player.participant.role)


class TAS(Page):
    form_model = 'player'
    form_fields = [
        'amb1',
        'amb2',
        'amb3',
        'amb4',
        'amb5',
        'amb6',
        'amb7',
        'amb8',
        'amb9',
        'amb10',
    ]

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.payoff = 200


class Debriefing(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            total_earnings=player.payoff.to_real_world_currency(player.session)
        )


page_sequence = [
    Showup,
    TAS,
    Debriefing,
]
