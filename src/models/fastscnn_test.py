git clone https://github.com/Tramac/Fast-SCNN-pytorch.git
cd Fast-SCNN-pytorch
pip install -r requirements.txt

python demo.py --cpu --weight-path ./pretrained/fast_scnn_citys.pth --img-path ./samples/demo.png
