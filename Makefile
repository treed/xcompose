SHELL = "/bin/bash"

json:
	./tools/prepareJSON "source/keybindings.json" "build/keybindings.json"

xcompose: json
	./tools/generateXCompose "build/keybindings.json" "build/dotXCompose"

install: xcompose
	./tools/install

clean:
	rm build/*