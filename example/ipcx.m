classdef ipcx
    properties (Access = public)
        msg = ""
    end
    
    
    methods (Access = public)
        
        function on(obj)
            rosinit
        end
        
        function off(obj)
            rosshutdown
        end
        
        function sub = subscribe(obj,topic,show)
            if nargin == 2
                %default
                sub = rossubscriber(topic, @dispFx);
            elseif nargin == 3
                if show == "on"
                    sub = rossubscriber(topic, @dispFx);
                elseif show == "off"
                    sub = rossubscriber(topic);
                end
            end            
        end
      
       function sub = subscribe2(obj,topic,func)
                
           sub = rossubscriber(topic, func);
          
        end
        
        
    end
end


function dispFx(src,msg)         
   disp(msg.Data)
end


