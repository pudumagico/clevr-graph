
import yaml
import sys

# LineProperties = {
# 	"has_aircon": [True, False],
# 	"color": ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'olive', 'cyan'],
# 	# "stroke": ["solid" , "dashed", "dashdot", "dotted"],
# 	"stroke": ["solid"],
# 	"built": ["50s", "60s", "70s", "80s", "90s", "00s", "recent"],
# }

# StationProperties = {
# 	"disabled_access": [True, False],
# 	"has_rail": [True, False],
# 	"music": ["classical", "rock n roll", "rnb", "electronic", "country", "none", "swing", "pop"],
# 	"architecture": ["victorian", "modernist", "concrete", "glass", "art-deco", "new"],
# 	"size": ["tiny", "small", "medium-sized", "large", "massive"],
# 	"cleanliness": ["clean", 'dirty', 'shabby', 'derilict', 'rat-infested'],
# }

# OtherProperties = {
# 	"surname": [" street", " st", " road", " court", " grove", "bridge", " bridge", " lane", " way", " boulevard", " crossing", " square", "ham", ' on trent', ' upon Thames', ' international', ' hospital', 'neyland', 'ington', 'ton', 'wich', ' manor', ' estate', ' palace']
# }

colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'olive', 'cyan']


radius = 3
img_size = 1000

node_radius = 2*100*16/(72* (img_size) )

if __name__ == "__main__":
        
    with open(sys.argv[1], "r") as file:
        docs = yaml.load_all(file, yaml.FullLoader)
        # data = yaml.safe_load(file)
        # print(data['graph'].keys())
        for data in docs:
            # print(data)
            with open('data/train/graph-' + str(data['graph']['id']) + '.txt', 'w') as datafile:
                    
                station_pixel_pos = {}

                for node in data['graph']['nodes']:
                    x_mean = (radius + node['x']) / (2 * radius)
                    y_mean = (radius - node['y']) / (2 * radius)
                    # print(node)
                    # print(node['id'],x,y)
                    station_pixel_pos[node['id']] = (x_mean, y_mean)

                    cls = 0
                                
                    datafile.write(' '.join([str(cls), str(x_mean), str(y_mean), str(node_radius), str(node_radius)]) + '\n')

                for edge in data['graph']['edges']:
                    # x = round((radius + node['x']) * img_size / (2 * radius))
                    # y = round((radius - node['y']) * img_size / (2 * radius))
                    # print(edge)
                    s1 = edge['station1']
                    s2 = edge['station2']

                    x1, y1 = station_pixel_pos[s1]
                    x2, y2 = station_pixel_pos[s2]

                    x_mean = (x1 + x2)/2
                    y_mean = (y1 + y2)/2

                    width = x2 - x1 if x2 > x1 else x1 - x2
                    height = y2 - y1 if y2 > y1 else y1 - y2

                    color = edge['line_color']

                    cls = 1 + colors.index(color)

                    datafile.write(
                        ' '.join([str(cls), str(x_mean), str(y_mean), str(width), str(height)]) + '\n')
