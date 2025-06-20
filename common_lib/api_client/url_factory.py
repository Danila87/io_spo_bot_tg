class URLFactory:
    def __init__(
            self,
            host:str,
            port: int
    ):
        self._host = host
        self._port = port


    @property
    def base_url(self):
        return f'{self._host}:{self._port}'

    @property
    def base_url_song(self):
        return f'{self.base_url}/song'

    @property
    def base_url_piggy_bank(self):
        return f'{self.base_url}/piggy_bank'

    @property
    def base_url_methodical_book(self):
        return f'{self.base_url}/methodical_book'

    @property
    def base_url_song_categories(self):
        return f'{self.base_url_song}/categories'

    @property
    def song_category(self):
        return f'{self.base_url_song_categories}/'

    @property
    def base_url_service(self):
        return f'{self.base_url}/service'

    @property
    def search_by_title(self):
        return f'{self.base_url_service}/search_by_title/'

    @property
    def reviews(self):
        return f'{self.base_url_service}/reviews/'

    @property
    def all_songs(self):
        return f'{self.base_url_song}/songs'

    @property
    def sons_by_category(self):
        return f'{self.all_songs}/by_category/'

    @property
    def main_song_categories(self):
        return f'{self.base_url_song_categories}/mains'

    @property
    def childs_category(self):
        return f'{self.base_url_song_categories}/get_children/'

    @property
    def children_groups(self):
        return f'{self.base_url_piggy_bank}/groups'

    @property
    def games(self):
        return f'{self.base_url_piggy_bank}/games/'

    @property
    def game_file(self):
        return f'{self.games}file/'

    @property
    def games_by_type_group(self):
        return f'{self.games}by_type_group/'

    @property
    def game_types(self):
        return f'{self.base_url_piggy_bank}/types_game'

    @property
    def legend_by_id(self):
        return f'{self.base_url_piggy_bank}/legends/'

    @property
    def legend_file(self):
        return f'{self.legend_by_id}file/'

    @property
    def legends_by_group(self):
        return f'{self.base_url_piggy_bank}/legend/by_group/'

    @property
    def ktd(self):
        return f'{self.base_url_piggy_bank}/ktd'

    @property
    def ktd_by_id(self):
        return f'{self.ktd}/'

    @property
    def ktds_by_group(self):
        return f'{self.ktd_by_id}by_group/'

    @property
    def ktd_file(self):
        return f'{self.ktd_by_id}file/'

    @property
    def chapters(self):
        return f'{self.base_url_methodical_book}/chapters/'

    @property
    def chapters_main(self):
        return f'{self.chapters}mains'

    @property
    def chapters_children(self):
        return f'{self.chapters}get_children/'

    @property
    def chapters_file(self):
        return f'{self.chapters}file/'

    @property
    def check_user(self):
        return f'{self.base_url_service}/check_user'

    @property
    def statistic(self):
        return f'{self.base_url}/statistic'

    @property
    def dashboards(self):
        return f'{self.statistic}/dashboards'

    @property
    def bot_dashboards(self):
        return f'{self.dashboards}/bot'

    def visualisation(self, dashboard_uid: str):
        return f'{self.dashboards}/{dashboard_uid}/visualisations'

    def visualisation_imp(self, dashboard_uid: str, visualisation_id: int):
        return f'{self.visualisation(dashboard_uid)}/{visualisation_id}/img'