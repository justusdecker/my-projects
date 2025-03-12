public class Main {
    public static void main(String[] args) {
        boolean is_running = true;
        byte[][] grid = {{0,0,0},{0,0,0},{0,0,0}};
        var input = new java.util.Scanner(System.in);
        byte[] players = {1,-1};
        boolean current_player = false;
        boolean is_occupied = false;
        while (is_running) {
            String user_input = "";
            boolean numeric = false;
            boolean is_in_field = false;
            while (user_input.isEmpty() || !numeric || !is_in_field || is_occupied) {
                Essentials.render_grid(grid);
                System.out.println("Player " + Byte.toString(players[current_player ? 1:0]) + " Enter your position: ");
                user_input = input.nextLine();

                numeric = Essentials.is_decimal(user_input);
                if (!numeric) continue;
                is_in_field = Essentials.check_field_position(user_input);
                if (!is_in_field) continue;
                is_occupied = Essentials.is_occupied(grid,user_input);

            }
            byte[] field_position = Essentials.get_field_position(user_input);
            grid[field_position[0]-1][field_position[1]-1] = players[current_player ? 1:0];
            if (Essentials.check_winner(grid) != 0) {
                return;
            }

            current_player = !current_player;
        }
    }

}
class Essentials {
    public static void render_grid(byte[][] grid) {
        String line = "";
        for (int i = 0;i < 3;i++) {
            line = "";
            for (int j = 0;j < 3;j++) {
                if (grid[i][j] == 1) {
                    line += "X";
                } else if (grid[i][j] == -1) {
                    line += "O";
                } else {
                    line += " ";
                }
            }
            System.out.println(line);
        }

    }
    public static boolean is_occupied(byte[][] grid, String number) {
        byte[] position = Essentials.get_field_position(number);
        return grid[position[0]-1][position[1]-1] != 0;
    }
    public static boolean is_decimal(String number) {
        try {
            Integer.parseInt(number);
            return true;
        }
        catch (NumberFormatException e) {
            System.out.println("Your value is not a number!");
            return false;
        }
    }
    public static byte check_winner(byte[][] grid) {
        byte points = 0;
        byte y_points = 0;
        int lr_points = grid[0][0] + grid[1][1] + grid[2][2];
        int rl_points = grid[0][2] + grid[1][1] + grid[2][0];

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                points += grid[i][j];
                y_points += grid[j][i];
            }

            if (points == 3 || points == -3 || y_points == 3 || y_points == -3) break;
            points = 0;
        }
        System.out.println(points);

        if (points == 3 || y_points == 3 || rl_points == 3 || lr_points == 3) {
            Essentials.render_grid(grid);
            System.out.println("Player 1 wins");
            return 1;
        } else if (points == -3 || y_points == -3 || rl_points == -3 || lr_points == -3) {
            Essentials.render_grid(grid);
            System.out.println("Player 2 wins");
            return 2;
        }

        return 0;
    }
    public static byte[] get_field_position(String number) {
        return new byte[]{
                Byte.parseByte(Character.toString(number.charAt(0))),
                Byte.parseByte(Character.toString(number.charAt(1)))
        };
    }
    public static boolean check_field_position(String number) {
        if (number.length() != 2) return false;
        byte[] position = Essentials.get_field_position(number);
        return position[0] <= 3 && position[1] <= 3 && position[0] > 0 && position[1] > 0;
    }
}