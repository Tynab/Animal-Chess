class GameState:
    def __init__(self):
        self.current_player = 'P'
        self.selected_piece = None
        self.game_over = False
        self.game_result = None
        self.pieces = {}
        self.images = {}

    def initialize(self):
        self.current_player = 'P'
        self.selected_piece = None
        self.game_over = False
        self.game_result = None
        self.pieces = self.load_initial_pieces()

    def load_initial_pieces(self):
        positions = {
            'C': [(0, 0), (6, 0), (1, 1), (5, 1), (0, 2), (2, 2), (4, 2), (6, 2)],
            'P': [(6, 8), (0, 8), (5, 7), (1, 7), (6, 6), (4, 6), (2, 6), (0, 6)]
        }
        pieces = {}
        for side in ('C', 'P'):
            pieces[side] = {}
            for i, name in enumerate(('Lion', 'Tiger', 'Cat', 'Dog', 'Elephant', 'Wolf', 'Leopard', 'Rat')):
                pieces[side][name] = {'pos': positions[side][i], 'alive': True}
        return pieces

    def handle_piece_selection(self, mouse_pos):
        c, r = mouse_pos[0] // 100, mouse_pos[1] // 100
        for piece_name, piece_info in self.pieces[self.current_player].items():
            if piece_info['pos'] == (c, r) and piece_info['alive']:
                self.selected_piece = piece_name
                return True
        return False


    def handle_piece_move(self, mouse_pos):
        if not self.selected_piece:
            return False

        c, r = mouse_pos[0] // 100, mouse_pos[1] // 100  # Assuming SPAN = 100
        start_pos = self.pieces[self.current_player][self.selected_piece]['pos']
        if self.is_move_valid(self.selected_piece, start_pos, (c, r)):
            self.pieces[self.current_player][self.selected_piece]['pos'] = (c, r)
            self.switch_player()
            self.selected_piece = None
            return True
        return False


    def check_game_end(self):
        # Check if any of 'C's pieces has entered 'P's den
        for piece_info in _pieces['C'].values():
            if piece_info['pos'] == DENS['P']:
                _game_over = True
                _game_result = 'YOU\nLOSE!!!'
                return

        # Check if any of 'P's pieces has entered 'C's den
        for piece_info in _pieces['P'].values():
            if piece_info['pos'] == DENS['C']:
                _game_over = True
                _game_result = 'YOU\nWIN!!!'
                return
