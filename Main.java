
public class Main {
    public class Grid {
        ArrayList<String> list = new ArrayList<>();
        int X_score = 0;
        int O_score = 0;

        public Grid(int numStrings) {
            this.X_score = 0;
            for (int i = 0; i < numStrings; i++) {
                list.add("String " + (i + 1));
            }
        }

        public int GridLength() {
            return list.size();
        }

        public void printGrid() {
            for (int i = 0; i < GridLength(); i++) {
                System.out.println(list.get(i));
            }
        }

        public void X(int x, int y) {
            int element = x + (y - 1) * (3);
            list.set(element, "X");
        }
    }

    public static void main(String[] args) {
        Grid grid = new Grid(3);
        grid.printGrid();
        grid.X(1, 2);
        grid.printGrid();

    }
}
