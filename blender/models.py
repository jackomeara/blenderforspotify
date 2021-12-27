from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator

lgenres = [
      "acoustic",
      "afrobeat",
      "alt-rock",
      "alternative",
      "ambient",
      "anime",
      "black-metal",
      "bluegrass",
      "blues",
      "bossanova",
      "brazil",
      "breakbeat",
      "british",
      "cantopop",
      "chicago-house",
      "children",
      "chill",
      "classical",
      "club",
      "comedy",
      "country",
      "dance",
      "dancehall",
      "death-metal",
      "deep-house",
      "detroit-techno",
      "disco",
      "disney",
      "drum-and-bass",
      "dub",
      "dubstep",
      "edm",
      "electro",
      "electronic",
      "emo",
      "folk",
      "forro",
      "french",
      "funk",
      "garage",
      "german",
      "gospel",
      "goth",
      "grindcore",
      "groove",
      "grunge",
      "guitar",
      "happy",
      "hard-rock",
      "hardcore",
      "hardstyle",
      "heavy-metal",
      "hip-hop",
      "holidays",
      "honky-tonk",
      "house",
      "idm",
      "indian",
      "indie",
      "indie-pop",
      "industrial",
      "iranian",
      "j-dance",
      "j-idol",
      "j-pop",
      "j-rock",
      "jazz",
      "k-pop",
      "kids",
      "latin",
      "latino",
      "malay",
      "mandopop",
      "metal",
      "metal-misc",
      "metalcore",
      "minimal-techno",
      "movies",
      "mpb",
      "new-age",
      "new-release",
      "opera",
      "pagode",
      "party",
      "philippines-opm",
      "piano",
      "pop",
      "pop-film",
      "post-dubstep",
      "power-pop",
      "progressive-house",
      "psych-rock",
      "punk",
      "punk-rock",
      "r-n-b",
      "rainy-day",
      "reggae",
      "reggaeton",
      "road-trip",
      "rock",
      "rock-n-roll",
      "rockabilly",
      "romance",
      "sad",
      "salsa",
      "samba",
      "sertanejo",
      "show-tunes",
      "singer-songwriter",
      "ska",
      "sleep",
      "songwriter",
      "soul",
      "soundtracks",
      "spanish",
      "study",
      "summer",
      "swedish",
      "synth-pop",
      "tango",
      "techno",
      "trance",
      "trip-hop",
      "turkish",
      "work-out",
      "world-music"
    ]
genres = [(genre, genre) for genre in lgenres]

# Create your models here.
class CriteriaModel(models.Model):
  track1 = models.CharField(max_length=50)
  artist1 = models.CharField(max_length=50)
  genre1 = models.CharField(max_length=50,choices=genres)
  type4 = models.CharField(max_length=20, choices=[('artists', 'Artist'),('tracks', 'Track'),('genres', 'Genre')], blank=True)
  choice4 = models.CharField(max_length=50, blank=True)
  type5 = models.CharField(max_length=20, choices=[('artists', 'Artist'),('tracks', 'Track'),('genres', 'Genre')], blank=True)
  choice5 = models.CharField(max_length=50, blank=True)
  length = models.IntegerField(validators=[MaxValueValidator(100)])
  name = models.CharField(max_length=50)

  def validate_genres(self, value):
    if self.type4 == 'genres':
      if self.choice4 not in genres:
        raise ValidationError(
          _('%(genre)s is not a valid genre'), params={'genre':self.choice4},
        )
    if self.type5 == 'genres':
      if self.choice5 not in genres:
        raise ValidationError(
          _('%(genre)s is not a valid genre'), params={'genre':self.choice5},
        )