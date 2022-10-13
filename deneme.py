print "Merhaba , Yeniden Merhaba"

 public void insertion_sort(int[] dizi) 
   {
     for(int j = 1; j < dizi.Length; j++)
     {
        int key = dizi[j]; 
        int i = j - 1;  
        while (i >= 0 && dizi[i] > key) 
        {
          dizi[i + 1] = dizi[i]; 
           i = i - 1;  
        }
        dizi[i + 1] = key;
      }
    }
