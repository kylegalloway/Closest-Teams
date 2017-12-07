sc=listdlg('ListString',schools)
lo=locations(1:end,sc)
i=1
while i<3143
    
[r,short(i)]=min(lo(i,1:end));
i=i+1
end

i=1
while i<length(sc)+1
    sch(i)=schools(sc(i))
    i=i+1
end
i=1
while i<3143
    p(i)=sch(short(i));
    i=i+1
end
   p=transpose(p);
   i=1
   while i<length(sc)+1
       color(i)=c1(sc(i))
   i=i+1
   end
   w=0
   for i=1:length(sc)
       v(i)=0;
       for k=1:length(p)
          
       v(i)=v(i)+isequal(i,short(k));
       end
      if v(i)==0
          sch(i-w)=[]
          color(i-w)=[]
          w=w+1
      end
   end
   
     