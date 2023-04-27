import os
import json
from argparse import ArgumentParser
from clipper.method import nearest_k, first_match, work_seperator
from clipper import controller
from tqdm import tqdm

def main(args):
    target = args.target
    clip_type = args.type
    size = args.size
    offset = args.offset
    n_size = args.n
    
    save_path = f'./saves/{clip_type}-{size}/{target}'
    os.makedirs(save_path, exist_ok=True)
    
    train = controller.Controller(target, 'train', clip_type, size, offset, n_size)
    train_result = train.nearest_k()
    with open(f'{save_path}/train.json', 'w') as f:
        json.dump(train_result, f)
    
    dev = controller.Controller(target, 'dev', clip_type, size, offset, n_size)
    dev_result = dev.nearest_k()
    with open(f'{save_path}/dev.json', 'w') as f:
        json.dump(dev_result, f)
    
    test = controller.Controller(target, 'test', clip_type, size, offset, n_size)
    test_result = test.nearest_k()
    with open(f'{save_path}/test.json', 'w') as f:
        json.dump(test_result, f)

if __name__ == '__main__':
    parser = ArgumentParser(description='Kakuyomu-Clipper')
    
    parser.add_argument('--target', type=int, default=42)
    parser.add_argument('--type', type=str, default='first-match')
    parser.add_argument('--size', type=int, default=5)
    parser.add_argument('--offset', type=int, default=256)
    parser.add_argument('--n', type=int, default=100)
    
    args = parser.parse_args()
    main(args)