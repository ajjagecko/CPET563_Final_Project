import cv2
import numpy as np
import argparse

focal_length = 6 #focal length in mm 
sensor_width = 12 #sensor width 12mm
baseline = 0.6 # baseline 60cm
camera_pos = 11 #camera position - 11away from the court

def ball_detect_algo(image_dir, label=''):
    ball_image = cv2.imread(image_dir)
    grayscale_img = cv2.cvtColor(ball_image,cv2.COLOR_BGR2GRAY)
    GaussianBlur_img = cv2.GaussianBlur(grayscale_img, (7,7), 1.5)
    #edge_de_img = cv2.canny(GaussianBlur_img, 30, 100)

    #debugger images
    #cv2.imshow(f'{label} grayscale image', grayscale_img)
    #cv2.imshow(f'{label} Gaussian blur image',GaussianBlur_img)
    #cv2.imshow(f'{label} canny edge detection', edge_de_img)

    #find the ball
    tennis_ball = cv2.HoughCircles(
        GaussianBlur_img,
        cv2.HOUGH_GRADIENT,
        dp=1.0,            
        minDist=10,       
        param1=30,         
        param2=6,         
        minRadius=1,       
        maxRadius=30  
    )

    if tennis_ball is not None:
        tennis_ball = np.uint16(np.around(tennis_ball))
        x,y,r = tennis_ball[0][0]

        #cv2.circle(ball_image, (x,y),r,(0,255,0), 2)
        #cv2.circle(ball_image, (x,y),2, (0,0,255),3)
        #cv2.imshow(f'{label} tennis ball found', ball_image)
        
        return x,y,r,ball_image.shape[1], ball_image.shape[0]
    else:   
        print("No ball found.")
        return -100, -100, -100, None, None

def depth_calculation(x_left,y_left,x_right,y_right, image_width,image_height,
                      focal_l = focal_length, sensor_w = sensor_width,
                      baseline_m = baseline, camera_z = camera_pos):
    #convert to pixel
    focal_length_px = (focal_l/sensor_w)*image_width
    disparity = float(x_left-x_right)
    if disparity == 0:
        return None
    
    camera_z = (focal_length_px * baseline_m) /disparity

    cx = image_width/2
    cy = image_height/2
    x_pos = ((x_left - cx) *camera_z) / focal_length_px
    y_pos = -((y_left - cy) *camera_z)/focal_length_px
    Z_pos = camera_pos - camera_z

    return x_pos, y_pos, Z_pos

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-m", "--image",
                    help="Image String")
    ap.add_argument("-b", "--buffer", type=int, default=64,
               help="max buffer size")
    args = vars(ap.parse_args())

    if not args.get("image", False):
        filename = 'blender_L_im_1.jpg'
    # otherwise, grab a reference to the video file
    else: 
        filename = args["image"];

    x_left, y_left, radius_left, w_left, h_left = ball_detect_algo(filename, '')
    #x_right, y_right, radius_right,w_right,h_right = ball_detect_algo('right_image.png', 'right image')

    if None in (x_left,y_left,w_left):
        print("no ball detected")
    else:
        #pos = depth_calculation(x_left,y_left,x_right,y_right,w_left,h_left)
        #if pos: 
            #X, Y, Z = pos
            #print("\n X Y Z position")
            #print(f"   X = {X:.3f} m ")
            #print(f"   Y = {Y:.3f} m ")
            #print(f"   Z = {Z:.3f} m ")
        #else:
            #print("disparity too close to 0")
        matlab_dat = [x_left, y_left, radius_left]
        return matlab_dat
    #cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    center_rad = main()
            

