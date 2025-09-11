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
        return f'http://{self._host}:{self._port}'

    @property
    def base_url_song(self):
        return f'{self.base_url}/songs/'

    @property
    def search_song(self):
        return f'{self.base_url_song}search/'

    @property
    def base_url_song_category(self):
        return f'{self.base_url_song}categories/'

    @property
    def song_category_childrens(self):
        return f'{self.base_url_song_category}childrens/'

    @property
    def base_url_song_events(self):
        return f'{self.base_url_song}song-events/'

    @property
    def base_url_piggy_bank(self):
        return f'{self.base_url}/piggy_bank/'

    @property
    def piggy_bank_groups(self):
        return f'{self.base_url_piggy_bank}groups/'

    @property
    def piggy_bank_types_game(self):
        return f'{self.base_url_piggy_bank}types_game/'

    @property
    def base_url_games(self):
        return f'{self.base_url_piggy_bank}games/'

    @property
    def games_by_type_group(self):
        return f'{self.base_url_games}by_type_group/'

    @property
    def game_file(self):
        return f'{self.base_url_games}file/'

    @property
    def base_piggy_bank_legend(self):
        return f'{self.base_url_piggy_bank}legends/'

    @property
    def legends_by_group(self):
        return f'{self.base_piggy_bank_legend}by_group/'

    @property
    def legend_file(self):
        return f'{self.base_piggy_bank_legend}file/'

    @property
    def base_piggy_bank_ktd(self):
        return f'{self.base_url_piggy_bank}ktd/'

    @property
    def ktd_by_group(self):
        return f'{self.base_piggy_bank_ktd}by_group/'

    @property
    def ktd_file(self):
        return f'{self.base_piggy_bank_ktd}file/'

    @property
    def base_url_methodical_book(self):
        return f'{self.base_url}/methodical_book/'

    @property
    def methodical_book_childrens(self):
        return f'{self.base_url_methodical_book}childrens/'

    @property
    def methodical_book_file(self):
        return f'{self.base_url_methodical_book}file/'

    @property
    def base_url_statistic(self):
        return f'{self.base_url}/statistic/'

    @property
    def statistic_dashboards(self):
        return f'{self.base_url_statistic}dashboards/'

    @property
    def statistic_dashboards_img(self):
        return f'{self.base_url_statistic}img/'

    @property
    def statistic_visualisation(self):
        return f'{self.statistic_dashboards}visualisations/'

    @property
    def statistic_visualisation_img(self):
        return f'{self.statistic_visualisation}img/'

    @property
    def base_url_service(self):
        return f'{self.base_url}/service/'

    @property
    def base_url_reviews(self):
        return f'{self.base_url_service}reviews/'

    @property
    def check_user(self):
        return f'{self.base_url_service}check_user/'

    @property
    def search_by_title(self):
        return f'{self.base_url_service}search_by_title/'