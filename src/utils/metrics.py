import time

def measure_inference(model, input_tensor):
    start = time.time()
    with torch.no_grad():
        _ = model(input_tensor)
    end = time.time()
    return end - start, 1 / (end - start)
