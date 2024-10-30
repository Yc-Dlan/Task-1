import cv2

#photo display
def display_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("图片加载失败，请检查路径")
        return

    # namewindows
    cv2.namedWindow('Image Display', cv2.WINDOW_NORMAL)

    # show-f
    cv2.imshow('Image Display', image)

    # waitkey
    cv2.waitKey(0)

    # close
    cv2.destroyAllWindows()

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("使用方法: python display_image.py <image_path>")
    else:
        display_image(sys.argv[1])
