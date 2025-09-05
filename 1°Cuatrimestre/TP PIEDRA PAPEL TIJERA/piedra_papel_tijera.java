import javax.swing.JOptionPane;

public class piedra_papel_tijera{
    public static void main(String[] args) {
        
        int usuario = 0;
        int computadora = 0;


        for(int i=1;i<4; i++){
            int opcion1 = Integer.parseInt(JOptionPane.showInputDialog("Numero 1: Piedra - Numero 2: Papel - Numero 3: Tijera. \nIngrese un numero del 1 al 3"));
        
            Double random1 = Math.random();
            int computadora1;

            if(random1 <= 0.33){
                computadora1 = 1;
            }else if(random1 <= 0.66){
                computadora1 = 2;
            }else{
                computadora1 = 3;
            }

            JOptionPane.showMessageDialog(null, "Numero 1: Piedra - Numero 2: Papel - Numero 3: Tijera. \nLa computadora elije: " + computadora1);

            //Gana usuario
            if(opcion1 == 1 && computadora1 == 3){
                JOptionPane.showMessageDialog(null, "El ganador es Usted!!");
                usuario++;
            }else if(opcion1 == 2 && computadora1 == 1){
                JOptionPane.showMessageDialog(null, "El ganador es Usted!!");
                usuario++;
            }else if(opcion1 == 3 && computadora1 == 2){
                JOptionPane.showMessageDialog(null, "El ganador es Usted!!");
                usuario++;
            }

            //Empate
            else if(opcion1 == 1 && computadora1 == 1){
                JOptionPane.showMessageDialog(null, "Es un empate");
            }else if(opcion1 == 2 && computadora1 == 2){
                JOptionPane.showMessageDialog(null, "Es un empate");
            }else if(opcion1 == 3 && computadora1 == 3){
                JOptionPane.showMessageDialog(null, "Es un empate");
            }

            //gana computadora
            else if(opcion1 == 3 && computadora1 == 1){
                JOptionPane.showMessageDialog(null, "La ganadora es la computadora");
                computadora++;
            }else if(opcion1 == 1 && computadora1 == 2){
                JOptionPane.showMessageDialog(null, "La ganadora es la computadora");
                computadora++;
            }else if(opcion1 == 2 && computadora1 == 3){
                JOptionPane.showMessageDialog(null, "La ganadora es la computadora");
                computadora++;
            }
        }

        if (computadora > usuario) {
            JOptionPane.showMessageDialog(null, "EL GANADOR DEL JUEGO ES COMPUTADORA");            
        }else if(computadora < usuario){
            JOptionPane.showMessageDialog(null, "EL GANADOR DEL JUEGO ES USTED");
        }else{
            JOptionPane.showMessageDialog(null, "ES UN EMPATE");
        }


        
    }
}