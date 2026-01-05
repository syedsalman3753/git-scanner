#sudo apt install python3-pip -y
#pip3 install truffleHog

RepoList=$(< $1)
branch=$2
max_depth=$3
rules=$4

if [[ $# -ne 4 ]]; then
    echo "parameters not provided;exiting"
    exit
fi

for repo in $RepoList; do
    echo "Scanning For $repo";
    trufflehog --branch $branch --max_depth $max_depth --entropy=False --rules $rules --regex  $repo --json > Reports/$(basename $repo).json
done


