FROM anasty17/mltb:latest
# FROM anasty17/mltb-oracle:latest

COPY . .

RUN useradd -m mltb
USER mltb

CMD ["bash", "start.sh"]
