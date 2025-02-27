import argparse

def process_gcode(file):

   # Read the input G-code
   with open(file, 'r') as input_file:
      lines = input_file.readlines()

   modified_lines = lines.copy()
   
   _START_PRINT_index = 0
   _START_PRINT_gcode = ""
   
   start_x_position = ""
   start_y_position = ""
   start_z_position = ""
   
   for line in modified_lines:
      if line.startswith("_START_PRINT_POSITION"):
         
         # Omit the newline character
         _START_PRINT_gcode = line.split('\n')[0]
         
         break

      _START_PRINT_index += 1
   
   for line in modified_lines:
      if line.startswith("G1 X"):

         # Split the gcode using spaces
         gcode_substr : list[str] = line.split(" ")
         
         # Remove the X and Y characters
         start_x_position = gcode_substr[1].split('X')[1]
         start_y_position = gcode_substr[2].split('Y')[1]
         
         break
      
   for line in modified_lines:
      if line.startswith("G1 Z"):

         # Split the gcode using spaces
         gcode_substr : list[str] = line.split(" ")
         
         # Remove the Z character
         start_z_position = gcode_substr[1].split('Z')[1]
         
         break
      
   modified_lines[_START_PRINT_index] = f"{_START_PRINT_gcode} START_POSITION_X={start_x_position} START_POSITION_Y={start_y_position} START_POSITION_Z={start_z_position}\n"
      
   # Overwrite the input file with the modified G-code
   with open(file, 'w') as output_file:
      output_file.writelines(modified_lines)

# Main execution
if __name__ == "__main__":
   
   parser = argparse.ArgumentParser(
      description = "G-code post-processor script for the custom _START_PRINT_POSITION macro from Klipper.",
   )
   
   parser.add_argument(
      "input_file",
      help = "Path to the input G-code file.",
   )
   
   parser.add_argument(
      "-first_layer_height",
      default = 0.2,
      help    = "First layer height of the print.",
   )
   
   args = parser.parse_args()
   
   process_gcode(
      file = args.input_file,
   )