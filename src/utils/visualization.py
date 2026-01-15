import matplotlib.pyplot as plt

def show_segmentation(input_img, output):
    plt.subplot(1,2,1); plt.imshow(input_img)
    plt.subplot(1,2,2); plt.imshow(output.argmax(1).squeeze(), cmap='jet')
    plt.show()
