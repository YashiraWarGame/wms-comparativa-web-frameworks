from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import BINARY, Column, DateTime, ForeignKey, Integer, Numeric, String, Table, Text, VARBINARY
from sqlalchemy.orm import relationship

db = SQLAlchemy()
Base = db.Model


class Ckanswertype(Base):
    __tablename__ = 'ckAnswerType'

    AnswerTypeID = Column(Integer, primary_key=True)
    Name = Column(String(64), nullable=False)
    Description = Column(String(255))

    def __unicode__(self):
        return self.Description


class Ckchallengecategory(Base):
    __tablename__ = 'ckChallengeCategory'

    ChallengeCategoryID = Column(Integer, primary_key=True)
    Name = Column(String(64), nullable=False)
    Description = Column(String(255))
    IconURL = Column(String(255))

    def __unicode__(self):
        return self.Description


class Ckchallengestatu(Base):
    __tablename__ = 'ckChallengeStatus'

    ChallengeStatusID = Column(Integer, primary_key=True)
    Name = Column(String(64), nullable=False)
    Description = Column(String(255))

    def __unicode__(self):
        return self.Description


class Ckscoretype(Base):
    __tablename__ = 'ckScoreType'

    ScoreTypeID = Column(Integer, primary_key=True)
    Name = Column(String(64), nullable=False)
    Description = Column(String(255))


class Pkanswer(Base):
    __tablename__ = 'pkAnswer'

    AnswerID = Column(Integer, primary_key=True)
    ChallengeID = Column(ForeignKey('pkChallenge.ChallengeID'), nullable=False, index=True)
    AnswerTypeID = Column(ForeignKey('ckAnswerType.AnswerTypeID'), nullable=False, index=True, server_default=u"'1'")
    Answer = Column(VARBINARY(256), nullable=False) #answers
    Salt = Column(BINARY(32), nullable=False)

    ckAnswerType = relationship(u'Ckanswertype')
    pkChallenge = relationship(u'Pkchallenge')

    def __repr__(self):
        return self.Answer


class Pkchallenge(Base):
    __tablename__ = 'pkChallenge'

    ChallengeID = Column(Integer, primary_key=True) #challengeID
    ChallengeCategoryID = Column(ForeignKey('ckChallengeCategory.ChallengeCategoryID'), nullable=False, index=True)
    ChallengeStatusID = Column(ForeignKey('ckChallengeStatus.ChallengeStatusID'), nullable=False, index=True, server_default=u"'0'")
    UserID = Column(Integer, nullable=False, server_default=u"'1'")
    Name = Column(String(32), nullable=False) #name
    Description = Column(Text, nullable=False) #description
    MaximumAttempts = Column(Integer, nullable=False, server_default=u"'1'") #maximumAttempts
    CreationDate = Column(DateTime, nullable=False) #creationDate
    PublicationDate = Column(DateTime) #publicationDate
    UpdateDate = Column(DateTime) #updateDate

    ckChallengeCategory = relationship(u'Ckchallengecategory')
    ckChallengeStatu = relationship(u'Ckchallengestatu')
    parents = relationship(
        u'Pkchallenge',
        secondary='rkRequiredChallenge',
        primaryjoin=u'Pkchallenge.ChallengeID == rkRequiredChallenge.c.ChallengeID',
        secondaryjoin=u'Pkchallenge.ChallengeID == rkRequiredChallenge.c.RequiredChallegeID'
    )

    def __unicode__(self):
        return self.Name

    @staticmethod
    def is_valid_answer(userAnswer):
        valid = False
        #filter(Pkanswer.AnswerID == userAnswerId).\
        possible_answers = Pkanswer.query.\
            join(Pkchallenge, Pkchallenge.ChallengeID == Pkanswer.ChallengeID).\
            join(Ckanswertype, Ckanswertype.AnswerTypeID == Pkanswer.AnswerTypeID). \
            with_entities(Pkchallenge.ChallengeID, Pkanswer.Answer, Pkanswer.Salt, Pkanswer.AnswerTypeID, Ckanswertype.Name).\
            all()
        for expected_answer in possible_answers:
            print(expected_answer.ChallengeID, expected_answer.AnswerTypeID, expected_answer.Name,
                  expected_answer.Answer, expected_answer.Salt)
            #print(expected_answer)
            #print dir(expected_answer)
            type_expected_answer = expected_answer.Name.upper()
            print type_expected_answer
            if type_expected_answer == 'HASH':
                import hashlib
                plain_text = userAnswer + expected_answer.Salt
                hash_result = hashlib.sha256(plain_text).hexdigest()
                #valid = hash_result == expected_answer.Answer #TODO: Bug en workbench no guarda bien blob
                valid = userAnswer == expected_answer.Answer
            elif type_expected_answer == 'REGEX':
                import re
                valid = bool(re.findall(r'^{}$'.format(expected_answer.Answer), userAnswer))

            else:
                raise Exception("Unsupported answer type")
            if valid:
                return True
        else:
            return False



class Skchallengescore(Pkchallenge):
    __tablename__ = 'skChallengeScore'

    ChallengeID = Column(ForeignKey('pkChallenge.ChallengeID'), primary_key=True, index=True)
    ScoreTypeID = Column(ForeignKey('ckScoreType.ScoreTypeID'), nullable=False, index=True)
    Score = Column(Numeric(6, 2), nullable=False)

    ckScoreType = relationship(u'Ckscoretype')


class RkRequiredChallenge(Base):
    __tablename__ = 'rkRequiredChallenge'

    ChallengeID = Column(ForeignKey('pkChallenge.ChallengeID'), primary_key=True, nullable=False, index=True)
    RequiredChallegeID = Column(ForeignKey('pkChallenge.ChallengeID'), primary_key=True, nullable=False, index=True)

