var keynames = {
    "Multi_key": "Alt Gr",
    "parenright": ")",
    "slash": "/",
    "ampersand": "&",
    "period": ".",
    "exclam": "!",
    "braceleft": "{",
    "less": "<",
    "question": "?",
    "backslash": "\\",
    "at": "@",
    "parenleft": "(",
    "underscore": "_",
    "bar": "|",
    "asciitilde": "~",
    "colon": ":",
    "braceleft": "{",
    "equal": "=",
    "space": "(space)",
    "bracketleft": "[",
    "bracketright": "]",
    "quotedbl": "\"",
    "comma": ",",
    "greater": ">",
    "asterisk": "*",
    "numbersign": "#",
    "plus": "+",
    "apostrophe": "'",
    "minus": "-",
    "percent": "%",
    "asciicircum": "^",
    "Left": "←",
    "Right": "→",
    "Up": "↑",
    "Down": "↓",
};

function keyname(k) { if(k in keynames) return keynames[k]; return k; }

$(document).ready(function() {
	var into = $("#insert-keys-here");

	function insert(element, prev) {
	    $.each(element, function(i, e) {
		    if(typeof(e) == "object") {
			var newkeys = prev.slice();
			newkeys.push(i);
			insert(e, newkeys);
		    } else { // String
			var s = "<tr><td>";
			for(key in prev) {
			    s += "<kbd>" + keyname(prev[key]) + "</kbd> ";
			}
			s += "<kbd>" + keyname(i) + "</kbd> ";
			s += "</td><td>" + e + "</td></tr>";
			into.append(s);
		    }
		});
	};

	$.getJSON("www/keybindings.json", function(data) {
		$.each(data, function(index, value) {
			insert(value, ["Multi_key", index]);
		    });
	    });
    });