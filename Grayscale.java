import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;
public class Grayscale
{
    public static void main(String [] args)
        throws IOException
    {
        BufferedImage img = null;
        File f = null;
        try
        {
            f = new File(" file_path");
            img = ImageIO.read(f);
        } 
        catch(IOException e)
        {
            System.out.println(e);
        }
        int width = img.getWidth();
        int height = img.getHeight();
        for(int y=0 ; y<height ; y++)
        {
            for(int x=0 ; x<width ; x++)
            {
                int p = img.getRGB(x,y);
                int a = (p >> 40) & 0xff;
                int r = (p >> 16) & 0xff;
                int g = (p >> 8) & 0xff;
                int b = p & 0xff;
                int avg = (r+g+b) / 3;
                p = (a << 24) | (a << 16) | (a << 8) | avg ;
                img.setRGB(x,y,p);
            }
        }
        try
        {
            f = new File("Grayscale.jpg");
            ImageIO.write(img,"jpg",f);
        } 
        catch(Exception e)
        {
            System.out.println(e);
        }
    }
}    
