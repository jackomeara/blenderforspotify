# Generated by Django 3.2.9 on 2021-12-19 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CriteriaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track1', models.CharField(max_length=50)),
                ('track2', models.CharField(blank=True, max_length=50)),
                ('track3', models.CharField(blank=True, max_length=50)),
                ('track4', models.CharField(blank=True, max_length=50)),
                ('track5', models.CharField(blank=True, max_length=50)),
                ('artist1', models.CharField(max_length=50)),
                ('artist2', models.CharField(blank=True, max_length=50)),
                ('artist3', models.CharField(blank=True, max_length=50)),
                ('artist4', models.CharField(blank=True, max_length=50)),
                ('artist5', models.CharField(blank=True, max_length=50)),
                ('genre1', models.CharField(choices=[('acoustic', 'acoustic'), ('afrobeat', 'afrobeat'), ('alt-rock', 'alt-rock'), ('alternative', 'alternative'), ('ambient', 'ambient'), ('anime', 'anime'), ('black-metal', 'black-metal'), ('bluegrass', 'bluegrass'), ('blues', 'blues'), ('bossanova', 'bossanova'), ('brazil', 'brazil'), ('breakbeat', 'breakbeat'), ('british', 'british'), ('cantopop', 'cantopop'), ('chicago-house', 'chicago-house'), ('children', 'children'), ('chill', 'chill'), ('classical', 'classical'), ('club', 'club'), ('comedy', 'comedy'), ('country', 'country'), ('dance', 'dance'), ('dancehall', 'dancehall'), ('death-metal', 'death-metal'), ('deep-house', 'deep-house'), ('detroit-techno', 'detroit-techno'), ('disco', 'disco'), ('disney', 'disney'), ('drum-and-bass', 'drum-and-bass'), ('dub', 'dub'), ('dubstep', 'dubstep'), ('edm', 'edm'), ('electro', 'electro'), ('electronic', 'electronic'), ('emo', 'emo'), ('folk', 'folk'), ('forro', 'forro'), ('french', 'french'), ('funk', 'funk'), ('garage', 'garage'), ('german', 'german'), ('gospel', 'gospel'), ('goth', 'goth'), ('grindcore', 'grindcore'), ('groove', 'groove'), ('grunge', 'grunge'), ('guitar', 'guitar'), ('happy', 'happy'), ('hard-rock', 'hard-rock'), ('hardcore', 'hardcore'), ('hardstyle', 'hardstyle'), ('heavy-metal', 'heavy-metal'), ('hip-hop', 'hip-hop'), ('holidays', 'holidays'), ('honky-tonk', 'honky-tonk'), ('house', 'house'), ('idm', 'idm'), ('indian', 'indian'), ('indie', 'indie'), ('indie-pop', 'indie-pop'), ('industrial', 'industrial'), ('iranian', 'iranian'), ('j-dance', 'j-dance'), ('j-idol', 'j-idol'), ('j-pop', 'j-pop'), ('j-rock', 'j-rock'), ('jazz', 'jazz'), ('k-pop', 'k-pop'), ('kids', 'kids'), ('latin', 'latin'), ('latino', 'latino'), ('malay', 'malay'), ('mandopop', 'mandopop'), ('metal', 'metal'), ('metal-misc', 'metal-misc'), ('metalcore', 'metalcore'), ('minimal-techno', 'minimal-techno'), ('movies', 'movies'), ('mpb', 'mpb'), ('new-age', 'new-age'), ('new-release', 'new-release'), ('opera', 'opera'), ('pagode', 'pagode'), ('party', 'party'), ('philippines-opm', 'philippines-opm'), ('piano', 'piano'), ('pop', 'pop'), ('pop-film', 'pop-film'), ('post-dubstep', 'post-dubstep'), ('power-pop', 'power-pop'), ('progressive-house', 'progressive-house'), ('psych-rock', 'psych-rock'), ('punk', 'punk'), ('punk-rock', 'punk-rock'), ('r-n-b', 'r-n-b'), ('rainy-day', 'rainy-day'), ('reggae', 'reggae'), ('reggaeton', 'reggaeton'), ('road-trip', 'road-trip'), ('rock', 'rock'), ('rock-n-roll', 'rock-n-roll'), ('rockabilly', 'rockabilly'), ('romance', 'romance'), ('sad', 'sad'), ('salsa', 'salsa'), ('samba', 'samba'), ('sertanejo', 'sertanejo'), ('show-tunes', 'show-tunes'), ('singer-songwriter', 'singer-songwriter'), ('ska', 'ska'), ('sleep', 'sleep'), ('songwriter', 'songwriter'), ('soul', 'soul'), ('soundtracks', 'soundtracks'), ('spanish', 'spanish'), ('study', 'study'), ('summer', 'summer'), ('swedish', 'swedish'), ('synth-pop', 'synth-pop'), ('tango', 'tango'), ('techno', 'techno'), ('trance', 'trance'), ('trip-hop', 'trip-hop'), ('turkish', 'turkish'), ('work-out', 'work-out'), ('world-music', 'world-music')], max_length=50)),
                ('genre2', models.CharField(blank=True, choices=[('acoustic', 'acoustic'), ('afrobeat', 'afrobeat'), ('alt-rock', 'alt-rock'), ('alternative', 'alternative'), ('ambient', 'ambient'), ('anime', 'anime'), ('black-metal', 'black-metal'), ('bluegrass', 'bluegrass'), ('blues', 'blues'), ('bossanova', 'bossanova'), ('brazil', 'brazil'), ('breakbeat', 'breakbeat'), ('british', 'british'), ('cantopop', 'cantopop'), ('chicago-house', 'chicago-house'), ('children', 'children'), ('chill', 'chill'), ('classical', 'classical'), ('club', 'club'), ('comedy', 'comedy'), ('country', 'country'), ('dance', 'dance'), ('dancehall', 'dancehall'), ('death-metal', 'death-metal'), ('deep-house', 'deep-house'), ('detroit-techno', 'detroit-techno'), ('disco', 'disco'), ('disney', 'disney'), ('drum-and-bass', 'drum-and-bass'), ('dub', 'dub'), ('dubstep', 'dubstep'), ('edm', 'edm'), ('electro', 'electro'), ('electronic', 'electronic'), ('emo', 'emo'), ('folk', 'folk'), ('forro', 'forro'), ('french', 'french'), ('funk', 'funk'), ('garage', 'garage'), ('german', 'german'), ('gospel', 'gospel'), ('goth', 'goth'), ('grindcore', 'grindcore'), ('groove', 'groove'), ('grunge', 'grunge'), ('guitar', 'guitar'), ('happy', 'happy'), ('hard-rock', 'hard-rock'), ('hardcore', 'hardcore'), ('hardstyle', 'hardstyle'), ('heavy-metal', 'heavy-metal'), ('hip-hop', 'hip-hop'), ('holidays', 'holidays'), ('honky-tonk', 'honky-tonk'), ('house', 'house'), ('idm', 'idm'), ('indian', 'indian'), ('indie', 'indie'), ('indie-pop', 'indie-pop'), ('industrial', 'industrial'), ('iranian', 'iranian'), ('j-dance', 'j-dance'), ('j-idol', 'j-idol'), ('j-pop', 'j-pop'), ('j-rock', 'j-rock'), ('jazz', 'jazz'), ('k-pop', 'k-pop'), ('kids', 'kids'), ('latin', 'latin'), ('latino', 'latino'), ('malay', 'malay'), ('mandopop', 'mandopop'), ('metal', 'metal'), ('metal-misc', 'metal-misc'), ('metalcore', 'metalcore'), ('minimal-techno', 'minimal-techno'), ('movies', 'movies'), ('mpb', 'mpb'), ('new-age', 'new-age'), ('new-release', 'new-release'), ('opera', 'opera'), ('pagode', 'pagode'), ('party', 'party'), ('philippines-opm', 'philippines-opm'), ('piano', 'piano'), ('pop', 'pop'), ('pop-film', 'pop-film'), ('post-dubstep', 'post-dubstep'), ('power-pop', 'power-pop'), ('progressive-house', 'progressive-house'), ('psych-rock', 'psych-rock'), ('punk', 'punk'), ('punk-rock', 'punk-rock'), ('r-n-b', 'r-n-b'), ('rainy-day', 'rainy-day'), ('reggae', 'reggae'), ('reggaeton', 'reggaeton'), ('road-trip', 'road-trip'), ('rock', 'rock'), ('rock-n-roll', 'rock-n-roll'), ('rockabilly', 'rockabilly'), ('romance', 'romance'), ('sad', 'sad'), ('salsa', 'salsa'), ('samba', 'samba'), ('sertanejo', 'sertanejo'), ('show-tunes', 'show-tunes'), ('singer-songwriter', 'singer-songwriter'), ('ska', 'ska'), ('sleep', 'sleep'), ('songwriter', 'songwriter'), ('soul', 'soul'), ('soundtracks', 'soundtracks'), ('spanish', 'spanish'), ('study', 'study'), ('summer', 'summer'), ('swedish', 'swedish'), ('synth-pop', 'synth-pop'), ('tango', 'tango'), ('techno', 'techno'), ('trance', 'trance'), ('trip-hop', 'trip-hop'), ('turkish', 'turkish'), ('work-out', 'work-out'), ('world-music', 'world-music')], max_length=50)),
                ('genre3', models.CharField(blank=True, choices=[('acoustic', 'acoustic'), ('afrobeat', 'afrobeat'), ('alt-rock', 'alt-rock'), ('alternative', 'alternative'), ('ambient', 'ambient'), ('anime', 'anime'), ('black-metal', 'black-metal'), ('bluegrass', 'bluegrass'), ('blues', 'blues'), ('bossanova', 'bossanova'), ('brazil', 'brazil'), ('breakbeat', 'breakbeat'), ('british', 'british'), ('cantopop', 'cantopop'), ('chicago-house', 'chicago-house'), ('children', 'children'), ('chill', 'chill'), ('classical', 'classical'), ('club', 'club'), ('comedy', 'comedy'), ('country', 'country'), ('dance', 'dance'), ('dancehall', 'dancehall'), ('death-metal', 'death-metal'), ('deep-house', 'deep-house'), ('detroit-techno', 'detroit-techno'), ('disco', 'disco'), ('disney', 'disney'), ('drum-and-bass', 'drum-and-bass'), ('dub', 'dub'), ('dubstep', 'dubstep'), ('edm', 'edm'), ('electro', 'electro'), ('electronic', 'electronic'), ('emo', 'emo'), ('folk', 'folk'), ('forro', 'forro'), ('french', 'french'), ('funk', 'funk'), ('garage', 'garage'), ('german', 'german'), ('gospel', 'gospel'), ('goth', 'goth'), ('grindcore', 'grindcore'), ('groove', 'groove'), ('grunge', 'grunge'), ('guitar', 'guitar'), ('happy', 'happy'), ('hard-rock', 'hard-rock'), ('hardcore', 'hardcore'), ('hardstyle', 'hardstyle'), ('heavy-metal', 'heavy-metal'), ('hip-hop', 'hip-hop'), ('holidays', 'holidays'), ('honky-tonk', 'honky-tonk'), ('house', 'house'), ('idm', 'idm'), ('indian', 'indian'), ('indie', 'indie'), ('indie-pop', 'indie-pop'), ('industrial', 'industrial'), ('iranian', 'iranian'), ('j-dance', 'j-dance'), ('j-idol', 'j-idol'), ('j-pop', 'j-pop'), ('j-rock', 'j-rock'), ('jazz', 'jazz'), ('k-pop', 'k-pop'), ('kids', 'kids'), ('latin', 'latin'), ('latino', 'latino'), ('malay', 'malay'), ('mandopop', 'mandopop'), ('metal', 'metal'), ('metal-misc', 'metal-misc'), ('metalcore', 'metalcore'), ('minimal-techno', 'minimal-techno'), ('movies', 'movies'), ('mpb', 'mpb'), ('new-age', 'new-age'), ('new-release', 'new-release'), ('opera', 'opera'), ('pagode', 'pagode'), ('party', 'party'), ('philippines-opm', 'philippines-opm'), ('piano', 'piano'), ('pop', 'pop'), ('pop-film', 'pop-film'), ('post-dubstep', 'post-dubstep'), ('power-pop', 'power-pop'), ('progressive-house', 'progressive-house'), ('psych-rock', 'psych-rock'), ('punk', 'punk'), ('punk-rock', 'punk-rock'), ('r-n-b', 'r-n-b'), ('rainy-day', 'rainy-day'), ('reggae', 'reggae'), ('reggaeton', 'reggaeton'), ('road-trip', 'road-trip'), ('rock', 'rock'), ('rock-n-roll', 'rock-n-roll'), ('rockabilly', 'rockabilly'), ('romance', 'romance'), ('sad', 'sad'), ('salsa', 'salsa'), ('samba', 'samba'), ('sertanejo', 'sertanejo'), ('show-tunes', 'show-tunes'), ('singer-songwriter', 'singer-songwriter'), ('ska', 'ska'), ('sleep', 'sleep'), ('songwriter', 'songwriter'), ('soul', 'soul'), ('soundtracks', 'soundtracks'), ('spanish', 'spanish'), ('study', 'study'), ('summer', 'summer'), ('swedish', 'swedish'), ('synth-pop', 'synth-pop'), ('tango', 'tango'), ('techno', 'techno'), ('trance', 'trance'), ('trip-hop', 'trip-hop'), ('turkish', 'turkish'), ('work-out', 'work-out'), ('world-music', 'world-music')], max_length=50)),
                ('genre4', models.CharField(blank=True, choices=[('acoustic', 'acoustic'), ('afrobeat', 'afrobeat'), ('alt-rock', 'alt-rock'), ('alternative', 'alternative'), ('ambient', 'ambient'), ('anime', 'anime'), ('black-metal', 'black-metal'), ('bluegrass', 'bluegrass'), ('blues', 'blues'), ('bossanova', 'bossanova'), ('brazil', 'brazil'), ('breakbeat', 'breakbeat'), ('british', 'british'), ('cantopop', 'cantopop'), ('chicago-house', 'chicago-house'), ('children', 'children'), ('chill', 'chill'), ('classical', 'classical'), ('club', 'club'), ('comedy', 'comedy'), ('country', 'country'), ('dance', 'dance'), ('dancehall', 'dancehall'), ('death-metal', 'death-metal'), ('deep-house', 'deep-house'), ('detroit-techno', 'detroit-techno'), ('disco', 'disco'), ('disney', 'disney'), ('drum-and-bass', 'drum-and-bass'), ('dub', 'dub'), ('dubstep', 'dubstep'), ('edm', 'edm'), ('electro', 'electro'), ('electronic', 'electronic'), ('emo', 'emo'), ('folk', 'folk'), ('forro', 'forro'), ('french', 'french'), ('funk', 'funk'), ('garage', 'garage'), ('german', 'german'), ('gospel', 'gospel'), ('goth', 'goth'), ('grindcore', 'grindcore'), ('groove', 'groove'), ('grunge', 'grunge'), ('guitar', 'guitar'), ('happy', 'happy'), ('hard-rock', 'hard-rock'), ('hardcore', 'hardcore'), ('hardstyle', 'hardstyle'), ('heavy-metal', 'heavy-metal'), ('hip-hop', 'hip-hop'), ('holidays', 'holidays'), ('honky-tonk', 'honky-tonk'), ('house', 'house'), ('idm', 'idm'), ('indian', 'indian'), ('indie', 'indie'), ('indie-pop', 'indie-pop'), ('industrial', 'industrial'), ('iranian', 'iranian'), ('j-dance', 'j-dance'), ('j-idol', 'j-idol'), ('j-pop', 'j-pop'), ('j-rock', 'j-rock'), ('jazz', 'jazz'), ('k-pop', 'k-pop'), ('kids', 'kids'), ('latin', 'latin'), ('latino', 'latino'), ('malay', 'malay'), ('mandopop', 'mandopop'), ('metal', 'metal'), ('metal-misc', 'metal-misc'), ('metalcore', 'metalcore'), ('minimal-techno', 'minimal-techno'), ('movies', 'movies'), ('mpb', 'mpb'), ('new-age', 'new-age'), ('new-release', 'new-release'), ('opera', 'opera'), ('pagode', 'pagode'), ('party', 'party'), ('philippines-opm', 'philippines-opm'), ('piano', 'piano'), ('pop', 'pop'), ('pop-film', 'pop-film'), ('post-dubstep', 'post-dubstep'), ('power-pop', 'power-pop'), ('progressive-house', 'progressive-house'), ('psych-rock', 'psych-rock'), ('punk', 'punk'), ('punk-rock', 'punk-rock'), ('r-n-b', 'r-n-b'), ('rainy-day', 'rainy-day'), ('reggae', 'reggae'), ('reggaeton', 'reggaeton'), ('road-trip', 'road-trip'), ('rock', 'rock'), ('rock-n-roll', 'rock-n-roll'), ('rockabilly', 'rockabilly'), ('romance', 'romance'), ('sad', 'sad'), ('salsa', 'salsa'), ('samba', 'samba'), ('sertanejo', 'sertanejo'), ('show-tunes', 'show-tunes'), ('singer-songwriter', 'singer-songwriter'), ('ska', 'ska'), ('sleep', 'sleep'), ('songwriter', 'songwriter'), ('soul', 'soul'), ('soundtracks', 'soundtracks'), ('spanish', 'spanish'), ('study', 'study'), ('summer', 'summer'), ('swedish', 'swedish'), ('synth-pop', 'synth-pop'), ('tango', 'tango'), ('techno', 'techno'), ('trance', 'trance'), ('trip-hop', 'trip-hop'), ('turkish', 'turkish'), ('work-out', 'work-out'), ('world-music', 'world-music')], max_length=50)),
                ('genre5', models.CharField(blank=True, choices=[('acoustic', 'acoustic'), ('afrobeat', 'afrobeat'), ('alt-rock', 'alt-rock'), ('alternative', 'alternative'), ('ambient', 'ambient'), ('anime', 'anime'), ('black-metal', 'black-metal'), ('bluegrass', 'bluegrass'), ('blues', 'blues'), ('bossanova', 'bossanova'), ('brazil', 'brazil'), ('breakbeat', 'breakbeat'), ('british', 'british'), ('cantopop', 'cantopop'), ('chicago-house', 'chicago-house'), ('children', 'children'), ('chill', 'chill'), ('classical', 'classical'), ('club', 'club'), ('comedy', 'comedy'), ('country', 'country'), ('dance', 'dance'), ('dancehall', 'dancehall'), ('death-metal', 'death-metal'), ('deep-house', 'deep-house'), ('detroit-techno', 'detroit-techno'), ('disco', 'disco'), ('disney', 'disney'), ('drum-and-bass', 'drum-and-bass'), ('dub', 'dub'), ('dubstep', 'dubstep'), ('edm', 'edm'), ('electro', 'electro'), ('electronic', 'electronic'), ('emo', 'emo'), ('folk', 'folk'), ('forro', 'forro'), ('french', 'french'), ('funk', 'funk'), ('garage', 'garage'), ('german', 'german'), ('gospel', 'gospel'), ('goth', 'goth'), ('grindcore', 'grindcore'), ('groove', 'groove'), ('grunge', 'grunge'), ('guitar', 'guitar'), ('happy', 'happy'), ('hard-rock', 'hard-rock'), ('hardcore', 'hardcore'), ('hardstyle', 'hardstyle'), ('heavy-metal', 'heavy-metal'), ('hip-hop', 'hip-hop'), ('holidays', 'holidays'), ('honky-tonk', 'honky-tonk'), ('house', 'house'), ('idm', 'idm'), ('indian', 'indian'), ('indie', 'indie'), ('indie-pop', 'indie-pop'), ('industrial', 'industrial'), ('iranian', 'iranian'), ('j-dance', 'j-dance'), ('j-idol', 'j-idol'), ('j-pop', 'j-pop'), ('j-rock', 'j-rock'), ('jazz', 'jazz'), ('k-pop', 'k-pop'), ('kids', 'kids'), ('latin', 'latin'), ('latino', 'latino'), ('malay', 'malay'), ('mandopop', 'mandopop'), ('metal', 'metal'), ('metal-misc', 'metal-misc'), ('metalcore', 'metalcore'), ('minimal-techno', 'minimal-techno'), ('movies', 'movies'), ('mpb', 'mpb'), ('new-age', 'new-age'), ('new-release', 'new-release'), ('opera', 'opera'), ('pagode', 'pagode'), ('party', 'party'), ('philippines-opm', 'philippines-opm'), ('piano', 'piano'), ('pop', 'pop'), ('pop-film', 'pop-film'), ('post-dubstep', 'post-dubstep'), ('power-pop', 'power-pop'), ('progressive-house', 'progressive-house'), ('psych-rock', 'psych-rock'), ('punk', 'punk'), ('punk-rock', 'punk-rock'), ('r-n-b', 'r-n-b'), ('rainy-day', 'rainy-day'), ('reggae', 'reggae'), ('reggaeton', 'reggaeton'), ('road-trip', 'road-trip'), ('rock', 'rock'), ('rock-n-roll', 'rock-n-roll'), ('rockabilly', 'rockabilly'), ('romance', 'romance'), ('sad', 'sad'), ('salsa', 'salsa'), ('samba', 'samba'), ('sertanejo', 'sertanejo'), ('show-tunes', 'show-tunes'), ('singer-songwriter', 'singer-songwriter'), ('ska', 'ska'), ('sleep', 'sleep'), ('songwriter', 'songwriter'), ('soul', 'soul'), ('soundtracks', 'soundtracks'), ('spanish', 'spanish'), ('study', 'study'), ('summer', 'summer'), ('swedish', 'swedish'), ('synth-pop', 'synth-pop'), ('tango', 'tango'), ('techno', 'techno'), ('trance', 'trance'), ('trip-hop', 'trip-hop'), ('turkish', 'turkish'), ('work-out', 'work-out'), ('world-music', 'world-music')], max_length=50)),
                ('length', models.IntegerField()),
            ],
        ),
    ]