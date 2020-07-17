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
        
        function sub = subscribe(obj,topic,func)
            if nargin == 2
                sub = rossubscriber(topic, @dispFx);
            elseif nargin == 3
                sub = rossubscriber(topic, func);
            end

            
        end
      
    end
end


function dispFx(src,msg)         
   disp(msg.Data)
end


