import java.util.Scanner;

public class Lab01b_ifelse {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
		double product1 = 0, product2 = 0, product3 = 0;
        int quantity, productNumber = -1;
        double total;
        while (productNumber !=0){
            System.out.println("Enter product number (1-3): ");
            System.out.println("Enter 0 to stop");
            productNumber = input.nextInt();

            if (productNumber !=0){
                System.out.print("Enter quantity sold: ");
                quantity = input.nextInt();

                if(productNumber == 1){
                    total = quantity * 2.98;
                    product1 = total + product1;
                }
                else if(productNumber == 2){
                    total = quantity * 4.50;
                    product2 = total + product2;
                }
                else if(productNumber == 3){
                    total = quantity * 9.98;
                    product3 = total + product3;
                }
                else{
                    System.out.println("Invalid choice, select a number between 1-3.");
                } 
            }
        }

        System.out.printf("Product 1: $%.2f\n", product1);
        System.out.printf("Product 2: $%.2f\n", product2);
        System.out.printf("Product 3: $%.2f\n", product3);

        input.close();

    }
}
