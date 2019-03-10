//
// Created by revetoon on 3/10/19.
//

#ifndef OBJPARSER_LRULECONTEXT_HH
#define OBJPARSER_LRULECONTEXT_HH


#include "LRule.hh"

class LRuleContext : public LRule {
public:
    LRuleContext(const std::vector<LNode> &precede, const std::vector<LNode> &start, const std::vector<LNode> &follow,
                 const std::vector<LNode> &finish);

    LRuleContext(const std::vector<LNode> &precede, const std::vector<LNode> &start, const std::vector<LNode> &follow,
                 const std::vector<LNode> &finish, const std::vector<LNode> &ignore);

public:
    bool accept(std::vector<LNode>::iterator it) override;

    std::vector<LNode> getResult() override;

private:

    bool acceptPrecede(const std::vector<LNode>::iterator &it);

    bool acceptFollow(const std::vector<LNode>::iterator &it);

    bool vectContains(const std::vector<LNode> &v, const LNode &n);

    void skipToMatchingBracket(std::vector<LNode>::iterator &it, bool reverse);
private:
    std::vector<LNode> precede;
    std::vector<LNode> start;
    std::vector<LNode> follow;
    std::vector<LNode> finish;
    std::vector<LNode> ignore;
};


#endif //OBJPARSER_LRULECONTEXT_HH