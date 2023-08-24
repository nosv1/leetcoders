class Solution {
public:
    bool isAnagram(string s, string t) {
        // check if length is same
        if (s.length() != t.length()) {
            return false;
        }

        // create a map to store the frequency of each character
        unordered_map<char, int> s_chars;
        unordered_map<char, int> t_chars;

        for (int i = 0; i < s.length(); i++) {
            char s_char = s[i];
            char t_char = t[i];

            if (s_chars.find(s_char) != s_chars.end()) {
                s_chars[s_char] += 1;
            } else {
                s_chars[s_char] = 1;
            }

            if (t_chars.find(t_char) != t_chars.end()) {
                t_chars[t_char] += 1;
            } else {
                t_chars[t_char] = 1;
            }
        }

        // the below loop uses auto to iterate through the map
        // 'it' is a pointer to the map
        // 'it->first' is the key
        // 'it->second' is the value
        for (auto it = s_chars.begin(); it != s_chars.end(); it++) {
            char key = it->first;
            int value = it->second;
            if (t_chars.find(key) == t_chars.end()) {
                return false;
            } else if (t_chars[key] != value) {
                return false;
            }
        }

        return true;
    }
};