import java.io.*;
public class C1{
	public static void main(String args[]) throws IOException{
		try{


		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		int s = Integer.parseInt(reader.readLine());
		for(int x = 0;x<s;x++){
			boolean p = false;
			int l = Integer.parseInt(reader.readLine());
			int c = Integer.parseInt(reader.readLine());

			String n = reader.readLine();
			String [] ns=n.split(" ");

			for(int x1=0;x1<c;x1++){
				for(int x2=0;x2<c;x2++){
					if(Integer.parseInt(ns[x1])+Integer.parseInt(ns[x2])==l && x1!=x2 && p==false){

						if(x1>x2){
							System.out.println(x2+1+" "+x1+1);
							p = true;
						}
						else{
							System.out.println(x1+1+" "+x2+1);
							p =true;

						}
					}
				}
			}
		}
	}
	catch(IOException ex){
		throw new IOException("asd");
	}
	}
}