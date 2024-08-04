while(start != end) do
if(Path_Ahead_Available) then
move forward
else if(Left_Turn_Available) then
Turn left
else if(Diffuser_Found) then
Diffuse Bombs
else
Turn right
end-if
if(Key_Found) then
Unlock Lock
end-if
end-while