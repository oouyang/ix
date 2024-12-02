apk add --update --no-cache bash git openssh-client yarn
mkdir ~/.ssh && touch ~/.ssh/id_rsa && chmod 600 ~/.ssh/id_rsa
ssh-keyscan -H github.com >> ~/.ssh/known_hosts
yarn global add vercel
# git clone git@github.com:oouyang/ix.git
# cd ix
mkdir .vercel && touch .vercel/project.json
git config --global user.email "oouyang@github.com"
git config --global user.name "oouyang"

# git add
# git commit 
# git push
#  vercel deploy --prod
echo done
