
fonts() {
gh release download v2.9.0 --repo yuru7/HackGen

brew tap homebrew/cask-fonts
brew install font-hack-nerd-font
}


zsh() {

# oh my zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
# start ship
curl -sS https://starship.rs/install.sh | sh

}
