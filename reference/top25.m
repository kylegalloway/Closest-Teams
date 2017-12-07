a=char()
a='{"groups":{'
i=0
k=1
b=a
l=1
schools=transpose(sch)
while i<length(schools)
  %  if colorsc(i+1)>-.1;
     %   q=num2str(colorsc(i+1));
    %else
   q=char(color(i+1));
    %end
   
    b=[b,'"#',q,'":{"div":"#box', num2str(i+1), '","label":"', char(schools(i+1)), '","paths":['];
     
    for k=1:3142
        if isequal(p(k),schools(i+1))==1;
            b=[b,'"',char(county(k)),'",'];
        end
 
    end
    b=b(1:end-1);
    b=[b,']},'];
    k=1;
    i=i+1
end
 b=b(1:end-1)
   b=[b,'},"title":"","hidden":[],"borders":"#000000"}']