import pcbnew
import math

def move_gr_line_endpoints(target_x, target_y, tolerance_mm=0.01):
    board = pcbnew.GetBoard()
    
    for item in board.GetDrawings():
        if isinstance(item, pcbnew.PCB_SHAPE) and item.GetShape() == pcbnew.SHAPE_T_SEGMENT:
            start = item.GetStart()
            start_x= pcbnew.ToMM(start.x)
            start_y= pcbnew.ToMM(start.y)
            
            end = item.GetEnd()
            end_x= pcbnew.ToMM(end.x)
            end_y= pcbnew.ToMM(end.y)
            
            #print(f"Target: {target_x}, {target_y}   Start: {start_x}, {start_y}   End: {end_x}, {end_y}")
            
            if abs(start_x - target_x) < tolerance_mm and abs(start_y - target_y) < tolerance_mm:
                item.SetStart(pcbnew.VECTOR2I(int(pcbnew.FromMM(target_x)), int(pcbnew.FromMM(target_y))))
                print(f"Moved GR_LINE Start: {start_x}, {start_y} to target={target_x}, {target_y}")
            
            if abs(end_x - target_x) < tolerance_mm and abs(end_y - target_y) < tolerance_mm:            
                item.SetEnd(pcbnew.VECTOR2I(int(pcbnew.FromMM(target_x)), int(pcbnew.FromMM(target_y))))
                print(f"Moved GR_LINE End: {end_x}, {end_y} to target={target_x}, {target_y}")

def correct_gr_line_at_via_locations():
    board = pcbnew.GetBoard()
    vias = [item for item in board.GetTracks() if isinstance(item, pcbnew.PCB_VIA)]

    print(f"Found {len(vias)} vias:")
    
    for via in vias:
        pos = via.GetPosition()
        x_mm = pcbnew.ToMM(pos.x)
        y_mm = pcbnew.ToMM(pos.y)
        #print(f"Via at X: {x_mm:.2f} mm, Y: {y_mm:.2f} mm")
        
        move_gr_line_endpoints(x_mm, y_mm, tolerance_mm=0.025)

correct_gr_line_at_via_locations()

# exec(open("C:\\WorkSpace\\Motor_Axial\\Software\\fix_via_trace_locations_in_kicad.py").read())
