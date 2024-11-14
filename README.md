Pulll the docker image: 
```bash
docker pull louiewang820/sign2text:latest
```
Run docker and attach the file folder to the container
```bash
sudo docker run --gpus all -it --rm \
--shm-size=8g \
--mount type=bind,source="$HOME/TwoStreamNetwork",target=/workspace \
-e PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True \
louiewang820/sign2text
```
download large files
```bash
cd workspace
python download_folder.py 
```
test inference
```bash
python -m torch.distributed.launch --nproc_per_node 1 --use_env prediction.py --config experiments/configs/TwoStream/phoenix-2014t_s2g.yaml
```
