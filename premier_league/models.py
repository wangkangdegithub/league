from django.db import models
class Article(models.Model):
    title=models.CharField(max_length=32)
    content=models.TextField()
    def __str__(self):
        return self.title

class Premier(models.Model):
    home = models.CharField(max_length=10)
    away = models.CharField(max_length=10)

class test(models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField()
    def __str__(self):
        return self.title


class season(models.Model):
    assists_away_team = models.FloatField(max_length=10)
    assists_home_team = models.FloatField(max_length=10)
    attendance = models.FloatField(max_length=10)
    away_goals = models.FloatField(max_length=10)
    away_team = models.CharField(max_length=32)
    blocks_away_team = models.FloatField(max_length=10)
    blocks_home_team = models.FloatField(max_length=10)
    clearances_away_team = models.FloatField(max_length=10)
    clearances_home_team = models.FloatField(max_length=10)
    corners_away_team = models.FloatField(max_length=10)
    corners_home_team = models.FloatField(max_length=10)
    crosses_away_team = models.FloatField(max_length=10)
    crosses_home_team = models.FloatField(max_length=10)
    date = models.CharField(max_length=32)
    fouls_away_team = models.FloatField(max_length=10)
    fouls_home_team = models.FloatField(max_length=10)
    free_kicks_away_team = models.FloatField(max_length=10)
    free_kicks_home_team = models.FloatField(max_length=10)
    handballs_away_team = models.FloatField(max_length=10)
    handballs_home_team = models.FloatField(max_length=10)
    home_goals = models.FloatField(max_length=10)
    home_team = models.CharField(max_length=32)
    offsides_away_team = models.FloatField(max_length=10)
    offsides_home_team = models.FloatField(max_length=10)
    penalties_away_team = models.FloatField(max_length=10)
    penalties_home_team = models.FloatField(max_length=10)
    red_cards_away_team = models.FloatField(max_length=10)
    red_cards_home_team = models.FloatField(max_length=10)
    saves_away_team = models.FloatField(max_length=10)
    saves_home_team = models.FloatField(max_length=10)
    shots_off_target_away_team = models.FloatField(max_length=10)
    shots_off_target_home_team = models.FloatField(max_length=10)
    shots_on_target_away_team = models.FloatField(max_length=10)
    shots_on_target_home_team = models.FloatField(max_length=10)
    throw_ins_away_team = models.FloatField(max_length=10)
    throw_ins_home_team = models.FloatField(max_length=10)
    total_shots_away_team = models.FloatField(max_length=10)
    total_shots_home_team = models.FloatField(max_length=10)
    yellow_cards_away_team = models.FloatField(max_length=10)
    yellow_cards_home_team = models.FloatField(max_length=10)
    def __str__(self):
        return self.home_team



